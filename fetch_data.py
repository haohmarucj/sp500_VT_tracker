import json, datetime
import yfinance as yf

# 在这里改成你实际关注的标的(指数或ETF代码)
FUNDS = [
    {"label": "标普500", "ticker": "^GSPC"},  # 也可改成 VOO / SPY
    {"label": "全球基金", "ticker": "VT"},      # 也可改成 VWRA.L 等
]

out = {"updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "funds": []}
for f in FUNDS:
    c = yf.Ticker(f["ticker"]).history(period="max", auto_adjust=False)["Close"].dropna()
    out["funds"].append({
        "label": f["label"],
        "ticker": f["ticker"],
        "price": round(float(c.iloc[-1]), 2),
        "date": str(c.index[-1].date()),
        "ath": round(float(c.max()), 2),
        "ath_date": str(c.idxmax().date()),
        "ma200": round(float(c.tail(200).mean()), 2),
    })

with open("data.json", "w", encoding="utf-8") as fp:
    json.dump(out, fp, ensure_ascii=False, indent=2)
print(json.dumps(out, ensure_ascii=False, indent=2))
