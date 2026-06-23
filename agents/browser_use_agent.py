from browser_use_sdk.v3 import AsyncBrowserUse
from dotenv import load_dotenv
from ast import literal_eval
import traceback

load_dotenv()

PROMPT_FILE = "prompts/extract_jobs.txt"


async def extract_jobs(company_url: str):

    print("\n" + "=" * 80)
    print(f"[AGENT] Processing company: {company_url}")
    print("=" * 80)

    # Load prompt
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        prompt = f.read()

    prompt = prompt.replace(
        "{company_url}",
        company_url
    )

    try:
        print("[AGENT] Creating Browser Use client...")
        client = AsyncBrowserUse()

        print("[AGENT] Running Browser Use...")
        result = await client.run(prompt)

        print("\n[AGENT] RAW RESULT TYPE:")
        print(type(result.output))

        print("\n[AGENT] RAW RESULT:")
        print(result.output)

        # CASE 1: Browser Use already returned a dict
        if isinstance(result.output, dict):

            print("\n[AGENT] Output is already a dictionary.")

            print(
                f"[AGENT] Jobs found: "
                f"{len(result.output.get('jobs', []))}"
            )

            return result.output

        # CASE 2: Output is string
        output = str(result.output)

        print("\n[AGENT] Output converted to string:")
        print(output)

        try:

            parsed = literal_eval(output)

            print("\n[AGENT] Successfully parsed string output.")

            print(
                f"[AGENT] Jobs found: "
                f"{len(parsed.get('jobs', []))}"
            )

            return parsed

        except Exception as parse_error:

            print("\n[AGENT] Failed to parse output.")
            print(parse_error)

            return {"jobs": []}

    except Exception as e:

        print("\n[AGENT] ERROR")
        print(e)

        traceback.print_exc()

        return {"jobs": []}