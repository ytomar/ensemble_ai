import requests
import yaml
from pathlib import Path


def ensemble_ai_home() -> Path:
    this_file = Path(__file__).parent
    home_dir = this_file / ".."
    return home_dir.absolute()


def get_config(name: str) -> dict:
    config_name = ensemble_ai_home() / "config" / f"{name}.yml"
    return yaml.load(open(config_name), Loader=yaml.SafeLoader)


def get_url(url: str, headers: dict=None):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"request to {url} failed with status_code {response.status_code}")

# def post_url(url: str, params: dict, headers: dict, data=None):
#     response = requests.post(url, params=params, headers=headers, data=data)


TEXT = """curl 'https://query1.finance.yahoo.com/v1/finance/search?q=NIFTY&lang=en-US&region=US&quotesCount=8&newsCount=0&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&enableCb=true&enableNavLinks=true&enableEnhancedTrivialQuery=true&enableCulturalAssets=true&enableLogoUrl=true&researchReportsCount=2' \
  -H 'authority: query1.finance.yahoo.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: GUC=AQEBCAFkeFlkokIfUwSP&s=AQAAAKu91_s4&g=ZHcWPw; A1=d=AQABBBrgWWQCEOwcAsk_Csckn73PvZULxXgFEgEBCAFZeGSiZFlQb2UB_eMBAAcIGuBZZJULxXg&S=AQAAApxmDx1U3f9yRT_gshYcnoY; A3=d=AQABBBrgWWQCEOwcAsk_Csckn73PvZULxXgFEgEBCAFZeGSiZFlQb2UB_eMBAAcIGuBZZJULxXg&S=AQAAApxmDx1U3f9yRT_gshYcnoY; cmp=t=1685526084&j=0&u=1---; PRF=t%3DGOLDBEES.NS%252BNIFTY_FIN_SERVICE.NS%26newChartbetateaser%3D1; A1S=d=AQABBBrgWWQCEOwcAsk_Csckn73PvZULxXgFEgEBCAFZeGSiZFlQb2UB_eMBAAcIGuBZZJULxXg&S=AQAAApxmDx1U3f9yRT_gshYcnoY' \
  -H 'sec-ch-ua: "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  --compressed"""