"""
meiji_dict.json 生成スクリプト
-------------------------------
明治期書簡語彙解釈補助辞典のJSONを生成する。
NaN（Excelの空欄）はnullとして明示的に保持し、
将来のCSV・DB変換およびNLP処理に接続可能な構造を維持する。
"""

import pandas as pd
import json
import math


def nan_to_none(obj):
    """floatのNaNをNoneに再帰的に変換する（JSON null対応）"""
    if isinstance(obj, float) and math.isnan(obj):
        return None
    elif isinstance(obj, dict):
        return {k: nan_to_none(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [nan_to_none(item) for item in obj]
    return obj


# --------------------------------------------------
# 1. Excel読み込み
# --------------------------------------------------
df = pd.read_excel("meiji_corpus_2026.xlsx")

# カラム名をJSON用に変更
df = df.rename(columns={
    "事例ID":           "case_id",
    "書簡番号":          "letter_id",
    "年月日":           "date",
    "表現（隠語・婉曲表現）": "expression",
    "意味解釈":          "interpretation",
    "本文抜粋":          "excerpt",
    "出来事タイプ":       "event_type",
    "関係人物":          "persons",
    "関連地名":         "places", 
    "出典①":           "source1",
    "出典②":           "source2"
})


# --------------------------------------------------
# 2. NaN → None（JSONではnullとして出力）
#    欠損値を明示的に保持し、「不明」等への置換は行わない。
#    欠損と「意図的な空欄」を区別可能にするため。
# --------------------------------------------------
data = nan_to_none(df.to_dict(orient="records"))


# --------------------------------------------------
# 3. JSON書き出し（allow_nan=Falseでnull出力を保証）
# --------------------------------------------------
with open("meiji_dict.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)

print(f"完了: {len(data)} 件を meiji_dict.json に書き出しました。")


# --------------------------------------------------
# 読み込み関数（将来の検索・分析・変換で再利用）
# --------------------------------------------------
def load_dict(path="meiji_dict.json") -> list[dict]:
    """
    meiji_dict.json を読み込み、辞書リストとして返す。
    nullはPythonのNoneとして保持される。
    """
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# 使用例（コメントアウト）
# data = load_dict()
#
# # 欠損チェック
# missing = [r for r in data if r["備考"] is None]
# print(f"備考が欠損しているエントリ数: {len(missing)}")
#
# # 特定人物で絞り込み
# yamagata = [r for r in data if r["related_people"] == "山県有朋"]
#
# # 将来: CSVへの変換
# import csv
# with open("meiji_dict.csv", "w", encoding="utf-8-sig", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)
