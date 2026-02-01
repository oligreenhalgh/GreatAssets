import base64
import json
import mimetypes
import os
from pathlib import Path
from typing import Optional

import requests


def interpret(
    pdf_path: str,
    *,
    api_key: Optional[str] = None,
    model: str = "gemini-2.5-flash",
    timeout_s: int = 120,
    output_json_path: Optional[str] = None,
) -> str:
    """
    Send an investment thesis PDF to Gemini and return a 5-sentence summary.
    """
    path = Path(pdf_path)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    mime_type, _ = mimetypes.guess_type(str(path))
    if mime_type != "application/pdf":
        raise ValueError(f"Expected a PDF file, got {mime_type or 'unknown'}")

    key = api_key or os.getenv("GEMINI_API_KEY") or "AIzaSyD2pmtgqZR0ISnGtRm_JzHL8kMsC2Wn72k"
    if not key:
        raise ValueError("Gemini API key is required")

    pdf_bytes = path.read_bytes()
    encoded_pdf = base64.b64encode(pdf_bytes).decode("ascii")

    prompt = (
        "You are an investment analyst reviewing the following investment thesis. Your task is to extract and summarize the thesis using only the format specified below. Do not add any introductory text, explanations, disclaimers, or concluding remarks. Do not restate the question. Do not include labels beyond those explicitly defined. Do not use bullet points. Do not include blank lines beyond those required by the format. If information is missing, infer cautiously from context. If inference is not possible, return an empty set [] for sectors and keep the summary factual and concise. Three things to consider are: 1. Do they want to buy or sell and what would be a sensible amount for them to sell / invest (based on the companies trading history), 2. What sectors (sector list: real estate, life science, defence, advanced manufacturing, clean energy, digital & tech, professional business, retail, creative industries, financial) do they have a high concentration of any specific asset sectors, and a summary. Required Output Format (exactly three lines): Line 1: xm (negative means sell amount, positive means invest amount), Line 2: sector1, sector2, ..., Line 3: 2–3 sentences summarizing the investment thesis, including timeline and KPIs if stated. Begin analysis only after reading the thesis and output only the formatted result."
    )

    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/{model}:generateContent?key={key}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"inline_data": {"mime_type": "application/pdf", "data": encoded_pdf}},
                    {"text": prompt},
                ]
            }
        ]
    }

    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=timeout_s,
    )
    response.raise_for_status()
    data = response.json()

    try:
        result_text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected response format: {data}") from exc

    if output_json_path:
        output_path = Path(output_json_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump({"output": result_text}, handle)

    return result_text

print(
    interpret(
        "/Users/finn/Documents/We recommend a net buy allocation of.pdf",
        output_json_path="/Users/finn/PycharmProjects/Hackathons/Finnovator25/Output/interpret_output.json",
    )
)
