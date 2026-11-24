# -*- coding: utf-8 -*-
"""
単語帳 501-600 完全データセット & 100問10択クイズ 自動生成スクリプト
- Excelブック (.xlsx):
    - Sheet 1: 単語帳一覧 (501-600)
    - Sheet 2: 10択クイズ (英→日) [出題順: 番号順]
    - Sheet 3: 10択クイズ (日→英) [出題順: 番号順]
- CSVファイル (BOM付きUTF-8 / Excel・Googleスプレッドシート両対応):
    - TOEIC_Words_501-600_List.csv (英単語と日本語訳が隣接)
    - TOEIC_100Quiz_EN_to_JA.csv
    - TOEIC_100Quiz_JA_to_EN.csv
"""

import os
import csv
import json
import shutil
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

from quiz_data import words_data, quiz_en_ja, quiz_ja_en, CHOICE_LABELS

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------------------------------------
# 1. Excel (.xlsx) 作成
# -------------------------------------------------------------
wb = openpyxl.Workbook()
wb.remove(wb.active)

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)
header_border = Border(
    left=Side(style='thin', color='94A3B8'),
    right=Side(style='thin', color='94A3B8'),
    top=Side(style='thin', color='94A3B8'),
    bottom=Side(style='medium', color='1E293B')
)
font_family = "Meiryo"

# --- Sheet 1: 単語帳一覧 ---
ws_words = wb.create_sheet(title="単語帳一覧(501-600)")
ws_words.views.sheetView[0].showGridLines = True
ws_words.freeze_panes = "A5"

ws_words.merge_cells("A1:G1")
ws_words["A1"] = "単語帳 重要単語一覧 (No. 501 - 600)"
ws_words["A1"].font = Font(name=font_family, size=15, bold=True, color="FFFFFF")
ws_words["A1"].fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
ws_words["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws_words.row_dimensions[1].height = 36

ws_words.merge_cells("A2:G2")
ws_words["A2"] = "収録語数: 全100語 | 出題範囲: 501〜600 | 例文・和訳・重要ポイント付き"
ws_words["A2"].font = Font(name=font_family, size=9, italic=True, color="475569")
ws_words["A2"].fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
ws_words["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws_words.row_dimensions[2].height = 22
ws_words.row_dimensions[3].height = 8

headers_words = ["No.", "英単語 (Word)", "主な意味 (Meaning)", "品詞", "例文 (Example Sentence)", "例文の日本語訳", "補足・関連語 (Notes)"]
ws_words.row_dimensions[4].height = 28
for col_num, h_text in enumerate(headers_words, 1):
    cell = ws_words.cell(row=4, column=col_num)
    cell.value = h_text
    cell.font = Font(name=font_family, size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = header_border

for r_idx, w in enumerate(words_data, start=5):
    ws_words.row_dimensions[r_idx].height = 25
    bg_color = "F8FAFC" if r_idx % 2 == 0 else "FFFFFF"
    fill_row = PatternFill(start_color=bg_color, end_color=bg_color, fill_type="solid")
    
    row_values = [
        w["no"], w["word"], w["meaning"], w["pos"],
        w["example_en"], w["example_ja"], w["notes"]
    ]
    for c_idx, val in enumerate(row_values, start=1):
        cell = ws_words.cell(row=r_idx, column=c_idx)
        cell.value = val
        cell.font = Font(name=font_family, size=10)
        cell.fill = fill_row
        cell.border = thin_border
        
        if c_idx == 1:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.font = Font(name=font_family, size=10, bold=True, color="1E3A8A")
        elif c_idx == 2:
            cell.alignment = Alignment(horizontal="left", vertical="center")
            cell.font = Font(name=font_family, size=10, bold=True)
        elif c_idx == 3:
            cell.alignment = Alignment(horizontal="left", vertical="center")
            cell.font = Font(name=font_family, size=10, bold=True, color="0F172A")
        elif c_idx == 4:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

col_widths_words = [8, 18, 22, 10, 45, 45, 45]
for i, w in enumerate(col_widths_words, 1):
    ws_words.column_dimensions[get_column_letter(i)].width = w

ws_words.auto_filter.ref = "A4:G104"

# --- クイズシート生成関数 ---
def build_quiz_sheet(sheet_title, main_title, quiz_data, is_en_to_ja=True):
    ws = wb.create_sheet(title=sheet_title)
    ws.views.sheetView[0].showGridLines = True
    ws.freeze_panes = "E6"
    
    ws.merge_cells("A1:T1")
    ws["A1"] = main_title
    ws["A1"].font = Font(name=font_family, size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 34
    
    for r in [2, 3]:
        ws.row_dimensions[r].height = 20
        for c in range(1, 21):
            ws.cell(row=r, column=c).fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    
    # 回答数
    ws.merge_cells("A2:B2")
    ws["A2"] = "回答数"
    ws["A2"].font = Font(name=font_family, size=9, bold=True, color="475569")
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("A3:B3")
    ws["A3"] = "=COUNTA(O6:O105)"
    ws["A3"].font = Font(name=font_family, size=13, bold=True, color="1E293B")
    ws["A3"].alignment = Alignment(horizontal="center", vertical="center")
    
    # 正解数
    ws.merge_cells("C2:D2")
    ws["C2"] = "正解数"
    ws["C2"].font = Font(name=font_family, size=9, bold=True, color="166534")
    ws["C2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("C3:D3")
    ws["C3"] = '=COUNTIF(P6:P105, "*正解*")'
    ws["C3"].font = Font(name=font_family, size=13, bold=True, color="166534")
    ws["C3"].alignment = Alignment(horizontal="center", vertical="center")
    
    # 正答率
    ws.merge_cells("E2:F2")
    ws["E2"] = "正答率"
    ws["E2"].font = Font(name=font_family, size=9, bold=True, color="1E3A8A")
    ws["E2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("E3:F3")
    ws["E3"] = '=IF(A3>0, C3/A3, 0)'
    ws["E3"].font = Font(name=font_family, size=13, bold=True, color="1E3A8A")
    ws["E3"].alignment = Alignment(horizontal="center", vertical="center")
    ws["E3"].number_format = "0.0%"
    
    # 使い方
    ws.merge_cells("G2:T2")
    ws["G2"] = "使い方: O列「あなたの回答」に 1〜0 の数字を入力してください（プルダウン選択可）。自動で正誤判定されます。"
    ws["G2"].font = Font(name=font_family, size=9, bold=True, color="0369A1")
    ws["G2"].alignment = Alignment(horizontal="left", vertical="center")
    
    ws.merge_cells("G3:T3")
    ws["G3"] = "出題順: No.501〜600の番号順 | 各問題の選択肢は10択ランダム配置 | 答え合わせ後は例文と解説で復習しましょう"
    ws["G3"].font = Font(name=font_family, size=8.5, italic=True, color="64748B")
    ws["G3"].alignment = Alignment(horizontal="left", vertical="center")
    
    ws.row_dimensions[4].height = 8
    ws.row_dimensions[5].height = 28
    
    quiz_headers = [
        ("問番号", "1E3A8A"),
        ("単語No.", "1E3A8A"),
        ("出題単語" if is_en_to_ja else "出題(意味)", "1E3A8A"),
        ("品詞", "1E3A8A"),
        ("選択肢 1", "0369A1"),
        ("選択肢 2", "0369A1"),
        ("選択肢 3", "0369A1"),
        ("選択肢 4", "0369A1"),
        ("選択肢 5", "0369A1"),
        ("選択肢 6", "0369A1"),
        ("選択肢 7", "0369A1"),
        ("選択肢 8", "0369A1"),
        ("選択肢 9", "0369A1"),
        ("選択肢 0", "0369A1"),
        ("あなたの回答 (1〜0)", "C2410C"),
        ("判定", "475569"),
        ("正解記号", "334155"),
        ("正解の意味" if is_en_to_ja else "正解の単語", "334155"),
        ("例文", "334155"),
        ("例文和訳", "334155"),
    ]
    
    for c_idx, (h_title, h_bg) in enumerate(quiz_headers, 1):
        c = ws.cell(row=5, column=c_idx)
        c.value = h_title
        c.font = Font(name=font_family, size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill(start_color=h_bg, end_color=h_bg, fill_type="solid")
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = header_border

    for q_idx, item in enumerate(quiz_data):
        row_num = q_idx + 6
        ws.row_dimensions[row_num].height = 24
        bg_color = "F8FAFC" if row_num % 2 == 0 else "FFFFFF"
        row_fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type="solid")
        
        q_target = item["word"] if is_en_to_ja else item["meaning"]
        
        ws.cell(row=row_num, column=1, value=f"Q{item['q_no']}").alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_num, column=2, value=item["no"]).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_num, column=3, value=q_target).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_num, column=4, value=item["pos"]).alignment = Alignment(horizontal="center", vertical="center")
        
        ws.cell(row=row_num, column=2).font = Font(name=font_family, size=10, bold=True, color="1E3A8A")
        ws.cell(row=row_num, column=3).font = Font(name=font_family, size=11, bold=True, color="0F172A")
        
        for choice_idx in range(10):
            c_cell = ws.cell(row=row_num, column=5 + choice_idx, value=item["choices"][choice_idx])
            c_cell.alignment = Alignment(horizontal="left", vertical="center")
            c_cell.font = Font(name=font_family, size=9)
        
        ans_cell = ws.cell(row=row_num, column=15)
        ans_cell.value = ""
        ans_cell.alignment = Alignment(horizontal="center", vertical="center")
        ans_cell.font = Font(name=font_family, size=12, bold=True, color="C2410C")
        ans_cell.fill = PatternFill(start_color="FFF7ED", end_color="FFF7ED", fill_type="solid")
        
        judge_cell = ws.cell(row=row_num, column=16)
        judge_cell.value = f'=IF(ISBLANK(O{row_num}), "", IF(TRIM(UPPER(O{row_num}))=TRIM(UPPER(Q{row_num})), "○ 正解", "× 不正解"))'
        judge_cell.alignment = Alignment(horizontal="center", vertical="center")
        judge_cell.font = Font(name=font_family, size=10, bold=True)
        
        ans_letter_cell = ws.cell(row=row_num, column=17, value=item["correct_letter"])
        ans_letter_cell.alignment = Alignment(horizontal="center", vertical="center")
        ans_letter_cell.font = Font(name=font_family, size=10, bold=True)
        
        correct_content = item["meaning"] if is_en_to_ja else item["word"]
        ws.cell(row=row_num, column=18, value=correct_content).alignment = Alignment(horizontal="left", vertical="center")
        ws.cell(row=row_num, column=19, value=item["example_en"]).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        ws.cell(row=row_num, column=20, value=item["example_ja"]).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        
        for col_idx in range(1, 21):
            cell = ws.cell(row=row_num, column=col_idx)
            cell.border = thin_border
            if col_idx not in [15]:
                cell.fill = row_fill
    
    dv = DataValidation(type="list", formula1='"1,2,3,4,5,6,7,8,9,0"', allow_blank=True)
    dv.error ='1から0の数字を選択してください。'
    dv.errorTitle = '入力エラー'
    dv.prompt = '選択肢(1〜0)を選んでください'
    dv.promptTitle = '回答の選択'
    ws.add_data_validation(dv)
    dv.add("O6:O105")
    
    green_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    green_font = Font(name=font_family, color="166534", bold=True)
    ws.conditional_formatting.add('P6:P105',
        CellIsRule(operator='equal', formula=['"○ 正解"'], stopIfTrue=True, fill=green_fill, font=green_font)
    )
    red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    red_font = Font(name=font_family, color="991B1B", bold=True)
    ws.conditional_formatting.add('P6:P105',
        CellIsRule(operator='equal', formula=['"× 不正解"'], stopIfTrue=True, fill=red_fill, font=red_font)
    )

    col_widths = {
        1: 6, 2: 9, 3: 16, 4: 8,
        5: 16, 6: 16, 7: 16, 8: 16, 9: 16, 10: 16, 11: 16, 12: 16, 13: 16, 14: 16,
        15: 18, 16: 12, 17: 10, 18: 18, 19: 35, 20: 35
    }
    for col_i, w_val in col_widths.items():
        ws.column_dimensions[get_column_letter(col_i)].width = w_val

build_quiz_sheet(
    sheet_title="10択クイズ(英→日)",
    main_title="単語帳 100問10択クイズ 【英単語 → 日本語の意味】 (出題順: 501〜600)",
    quiz_data=quiz_en_ja,
    is_en_to_ja=True
)

build_quiz_sheet(
    sheet_title="10択クイズ(日→英)",
    main_title="単語帳 100問10択クイズ 【日本語の意味 → 英単語】 (出題順: 501〜600)",
    quiz_data=quiz_ja_en,
    is_en_to_ja=False
)

excel_path = os.path.join(OUTPUT_DIR, "TOEIC_Words_501-600_100Quiz.xlsx")
try:
    wb.save(excel_path)
    print("Saved Excel:", excel_path)
except PermissionError:
    print(f"Notice: {excel_path} is open in Excel, skipped rewrite.")

# 旧ファイル名・和名ファイル名にもコピー保存
for alias_excel in ["TOEIC_Words_401-500_100Quiz.xlsx", "TOEIC単語501-600_100問10択クイズ.xlsx", "TOEIC単語401-500_100問10択クイズ.xlsx"]:
    try:
        shutil.copyfile(excel_path, os.path.join(OUTPUT_DIR, alias_excel))
        print(f"Copied Excel to {alias_excel}")
    except Exception as e:
        print(f"Could not copy to {alias_excel}: {e}")

# -------------------------------------------------------------
# 2. CSV 作成 (UTF-8 with BOM)
# -------------------------------------------------------------
csv_words_file = os.path.join(OUTPUT_DIR, "TOEIC_Words_501-600_List.csv")
try:
    with open(csv_words_file, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["No.", "英単語", "日本語訳", "品詞", "例文", "例文の日本語訳", "補足・関連語"])
        for w in words_data:
            writer.writerow([w["no"], w["word"], w["meaning"], w["pos"], w["example_en"], w["example_ja"], w["notes"]])
    print("Saved CSV List:", csv_words_file)
except PermissionError:
    print(f"Notice: {csv_words_file} is open in Excel, skipped rewrite.")

for alias_csv in ["TOEIC_Words_401-500_List.csv", "TOEIC単語一覧_501-600.csv", "TOEIC単語一覧_401-500.csv"]:
    try:
        shutil.copyfile(csv_words_file, os.path.join(OUTPUT_DIR, alias_csv))
        print(f"Copied CSV to {alias_csv}")
    except Exception as e:
        print(f"Could not copy to {alias_csv}: {e}")

# クイズCSV
csv_quiz_en_file = os.path.join(OUTPUT_DIR, "TOEIC_100Quiz_EN_to_JA.csv")
with open(csv_quiz_en_file, mode="w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "問題番号", "単語No.", "出題(英単語)", "品詞",
        "選択肢1", "選択肢2", "選択肢3", "選択肢4", "選択肢5",
        "選択肢6", "選択肢7", "選択肢8", "選択肢9", "選択肢0",
        "正解番号", "正解の意味", "例文", "例文和訳", "補足"
    ])
    for q in quiz_en_ja:
        writer.writerow([
            f"Q{q['q_no']}", q["no"], q["word"], q["pos"],
            q["choices"][0], q["choices"][1], q["choices"][2], q["choices"][3], q["choices"][4],
            q["choices"][5], q["choices"][6], q["choices"][7], q["choices"][8], q["choices"][9],
            q["correct_letter"], q["meaning"], q["example_en"], q["example_ja"], q["notes"]
        ])

for alias in ["TOEIC_100問10択クイズ_英日.csv"]:
    try:
        shutil.copyfile(csv_quiz_en_file, os.path.join(OUTPUT_DIR, alias))
    except Exception:
        pass

csv_quiz_ja_file = os.path.join(OUTPUT_DIR, "TOEIC_100Quiz_JA_to_EN.csv")
with open(csv_quiz_ja_file, mode="w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "問題番号", "単語No.", "出題(日本語の意味)", "品詞",
        "選択肢1", "選択肢2", "選択肢3", "選択肢4", "選択肢5",
        "選択肢6", "選択肢7", "選択肢8", "選択肢9", "選択肢0",
        "正解番号", "正解の単語", "例文", "例文和訳", "補足"
    ])
    for q in quiz_ja_en:
        writer.writerow([
            f"Q{q['q_no']}", q["no"], q["meaning"], q["pos"],
            q["choices"][0], q["choices"][1], q["choices"][2], q["choices"][3], q["choices"][4],
            q["choices"][5], q["choices"][6], q["choices"][7], q["choices"][8], q["choices"][9],
            q["correct_letter"], q["word"], q["example_en"], q["example_ja"], q["notes"]
        ])

for alias in ["TOEIC_100問10択クイズ_日英.csv"]:
    try:
        shutil.copyfile(csv_quiz_ja_file, os.path.join(OUTPUT_DIR, alias))
    except Exception:
        pass

print("=== All builds completed! ===")
