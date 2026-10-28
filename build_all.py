# -*- coding: utf-8 -*-
"""
TOEIC 401-500 完全データセット & 100問10択クイズ 自動生成スクリプト
- Excelブック (.xlsx):
    - Sheet 1: 単語帳一覧 (401-500)
    - Sheet 2: 10択クイズ (英→日) [出題順: 番号順]
    - Sheet 3: 10択クイズ (日→英) [出題順: 番号順]
- CSVファイル (BOM付きUTF-8 / Excel・Googleスプレッドシート両対応):
    - TOEIC_Words_401-500_List.csv
    - TOEIC_100Quiz_EN_to_JA.csv
    - TOEIC_100Quiz_JA_to_EN.csv
- HTML学習Webアプリ (発音機能・キーボード操作・復習機能):
    - TOEIC_100Quiz_App.html
"""

import os
import csv
import json
import random
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
random.seed(2026)

words_data = [
    {"no": 401, "word": "cause", "pos": "動詞", "meaning": "引き起こす", "example_en": "Heavy traffic is causing delays on Highway 18.", "example_ja": "18号線では交通渋滞により遅れが生じています。", "notes": "名: cause「原因、理由、大義」"},
    {"no": 402, "word": "decade", "pos": "名詞", "meaning": "10年", "example_en": "The city has changed over the last decade.", "example_ja": "その市はこの10年で変わった。", "notes": "ten yearsに言い換えることができる"},
    {"no": 403, "word": "expire", "pos": "動詞", "meaning": "期限が切れる", "example_en": "My passport has expired.", "example_ja": "私のパスポートは期限が切れた。", "notes": "名: expiration〈加米〉、expiry〈英〉「満了、終結」、expiration date「有効期限、使用期限」(=expiry date)"},
    {"no": 404, "word": "income", "pos": "名詞", "meaning": "収入", "example_en": "Tourism is the main source of income in the region.", "example_ja": "観光業はこの地域の主な収入源です。", "notes": "個人の「所得」という意味にもなる。同: revenue「収入」、反: expenditure「支出」"},
    {"no": 405, "word": "immediate", "pos": "形容詞", "meaning": "早急な", "example_en": "We need to take immediate action.", "example_ja": "私たちは早急な対応を取る必要があります。", "notes": "副: immediately「早急に」"},
    {"no": 406, "word": "questionnaire", "pos": "名詞", "meaning": "アンケート", "example_en": "Please complete the questionnaire after the seminar.", "example_ja": "セミナーのあと、アンケートにご記入ください。", "notes": "名: question「質問」、動: question「質問する、疑問に思う」"},
    {"no": 407, "word": "routine", "pos": "名詞", "meaning": "習慣的に繰り返されること", "example_en": "Exercise is part of my daily routine.", "example_ja": "運動は私の日課の一部です。", "notes": "「定められた手順」という意味もある。形: routine「決まった、いつもの」、副: routinely「いつものように」"},
    {"no": 408, "word": "transfer", "pos": "動詞", "meaning": "転勤する", "example_en": "Mr. Chen transferred from Taipei to Bangkok.", "example_ja": "チェンさんは台北からバンコクへ転勤した。", "notes": "「転勤させる、乗り換える、移す」などの意味もある。名: transfer「転勤、移動、乗り換え」"},
    {"no": 409, "word": "complicated", "pos": "形容詞", "meaning": "複雑な", "example_en": "Our evaluation system is very complicated.", "example_ja": "当社の評価システムはとても複雑です。", "notes": "同: complex「複雑な」、動: complicate「複雑にする」、名: complication「複雑にするもの」"},
    {"no": 410, "word": "education", "pos": "名詞", "meaning": "教育", "example_en": "The government has increased spending on education.", "example_ja": "政府は教育の支出を増やした。", "notes": "動: educate「教育する」、形: educational「教育的な」"},
    {"no": 411, "word": "greet", "pos": "動詞", "meaning": "出迎える", "example_en": "The manager greeted us with a smile.", "example_ja": "マネージャーは私たちを笑顔で出迎えてくれた。", "notes": "「あいさつする」という意味もある。名: greeting「あいさつ」"},
    {"no": 412, "word": "influence", "pos": "名詞", "meaning": "影響力", "example_en": "The former president still has influence over the company.", "example_ja": "元社長はまだ、会社に影響力を持っている。", "notes": "動: influence「影響を与える」(=affect)"},
    {"no": 413, "word": "lack", "pos": "名詞", "meaning": "不足", "example_en": "The project was canceled due to a lack of funds.", "example_ja": "資金不足のため、そのプロジェクトは中止になった。", "notes": "lack of ~「〜の不足」、同: shortage「不足」、動: lack「〜が足りない」"},
    {"no": 414, "word": "mild", "pos": "形容詞", "meaning": "温暖な", "example_en": "We had a mild winter this year.", "example_ja": "今年は暖冬だった。", "notes": "「軽い、マイルドな」などの意味もある。副: mildly「少し」(=slightly)"},
    {"no": 415, "word": "normally", "pos": "副詞", "meaning": "普通は", "example_en": "I normally work forty hours a week.", "example_ja": "私は普段、週に40時間働いています。", "notes": "同: usually「普通は」、形: normal「通常の」"},
    {"no": 416, "word": "physical", "pos": "形容詞", "meaning": "身体の", "example_en": "I need to do physical exercise regularly.", "example_ja": "私は定期的に身体的な運動をする必要がある。", "notes": "副: physically「身体的に」、名: physician「医師、内科医」"},
    {"no": 417, "word": "polite", "pos": "形容詞", "meaning": "礼儀正しい", "example_en": "The hotel clerk was polite and helpful.", "example_ja": "そのホテル従業員は礼儀正しく、親切だった。", "notes": "「丁寧な」という意味もある。副: politely「丁寧に、礼儀正しく」"},
    {"no": 418, "word": "population", "pos": "名詞", "meaning": "人口", "example_en": "What is the population of India?", "example_ja": "インドの人口はどのくらいですか。", "notes": "working population「労働人口」"},
    {"no": 419, "word": "pour", "pos": "動詞", "meaning": "注ぐ", "example_en": "She's pouring coffee into a cup.", "example_ja": "彼女はコーヒーをカップに注いでいる。", "notes": "「雨が激しく降る、殺到する、光が出る」などの意味もある。pour A into B「AをBに注ぐ」"},
    {"no": 420, "word": "instant", "pos": "形容詞", "meaning": "すぐの", "example_en": "The book was an instant success in California.", "example_ja": "その本はカリフォルニアで即座の成功を収めた。", "notes": "「（食品等が）インスタントの」という意味もある。同: immediate「すぐの」、名: instant「瞬間」、名: instance「事例」、for instance「例えば」(=for example)、副: instantly「すぐに」"},
    {"no": 421, "word": "venue", "pos": "名詞", "meaning": "会場", "example_en": "Be sure to arrive at the venue on time.", "example_ja": "必ず時間どおりに会場に到着するようにしてください。", "notes": "後ろに続く前置詞はfor。例: the venue for the event「イベント会場」"},
    {"no": 422, "word": "resign", "pos": "動詞", "meaning": "辞任する", "example_en": "The president resigned yesterday.", "example_ja": "社長は昨日、辞任した。", "notes": "名: resignation「辞任」、同: retire「退職する」、leave「辞める」、quit「辞める」"},
    {"no": 423, "word": "attach", "pos": "動詞", "meaning": "添付する", "example_en": "I attached the conference schedule for your information.", "example_ja": "ご参考までに会議スケジュールを添付いたしました。", "notes": "手紙、メールともに使う。「取り付ける、愛着を持たせる」などの意味もある。Attached is/are ~「〜が添付されています」、名: attachment「添付ファイル、付属品、愛着」"},
    {"no": 424, "word": "cancel", "pos": "動詞", "meaning": "取り消す", "example_en": "I'd like to cancel my reservation.", "example_ja": "予約の取り消しをお願いします。", "notes": "名: cancellation「取り消し、キャンセル」、同: call off「中止する」"},
    {"no": 425, "word": "common", "pos": "形容詞", "meaning": "よくある", "example_en": "It's a common spelling mistake.", "example_ja": "それはよくあるスペルミスです。", "notes": "「共通の」という意味もある。in common「共通して」、副: commonly「一般に、広く」"},
    {"no": 426, "word": "conversation", "pos": "名詞", "meaning": "会話", "example_en": "They're having a conversation.", "example_ja": "彼らは会話をしている。", "notes": "類: chat「（カジュアルな）会話」、動: converse「会話する」"},
    {"no": 427, "word": "economical", "pos": "形容詞", "meaning": "経済的な", "example_en": "It's more economical to buy in bulk.", "example_ja": "まとめて買うほうが経済的です。", "notes": "お金や時間などを節約できるという意味。同: economic「経済に関する」、名: economy「経済、節約」、副: economically「経済的に」"},
    {"no": 428, "word": "exchange", "pos": "動詞", "meaning": "交換する", "example_en": "Can I exchange this jacket for a black one?", "example_ja": "このジャケットを黒のものと交換することはできますか。", "notes": "「交わす」という意味もある。名: exchange「交換、交換品、取引所」、foreign exchange「外国為替」、stock exchange「証券取引所」"},
    {"no": 429, "word": "expert", "pos": "名詞", "meaning": "専門家", "example_en": "Peter is a computer expert.", "example_ja": "ピーターはコンピュータの専門家です。", "notes": "an expert in/on/at「〜の専門家」、名: expertise「専門技術・知識」（後ろに続く前置詞はin）"},
    {"no": 430, "word": "extension", "pos": "名詞", "meaning": "内線", "example_en": "What's your extension number?", "example_ja": "あなたの内線番号は何番ですか。", "notes": "「拡張、延長」などの意味もある。動: extend「伸ばす、広げる」"},
    {"no": 431, "word": "familiar", "pos": "形容詞", "meaning": "よく知っている", "example_en": "Are you familiar with this software?", "example_ja": "あなたはこのソフトウェアのことをよく知っていますか。", "notes": "familiar with ~「〜のことをよく知っている」、familiar to ~「〜にとってなじみがある」、名: familiarity「よく知っていること」"},
    {"no": 432, "word": "host", "pos": "動詞", "meaning": "主催する", "example_en": "The city hosts a music festival every year.", "example_ja": "その市は毎年、音楽祭を主催する。", "notes": "「番組の司会を務める」という意味もある。名: host「主催者、司会者」"},
    {"no": 433, "word": "ride", "pos": "名詞", "meaning": "車に乗せること", "example_en": "Can you give me a ride to the station?", "example_ja": "駅まで車に乗せていってもらえますか。", "notes": "give (人) a ride、動: ride「（乗り物に）乗る」"},
    {"no": 434, "word": "seek", "pos": "動詞", "meaning": "求める", "example_en": "We are seeking an accountant.", "example_ja": "当社は経理担当者を求めています。", "notes": "同: look for「探す」、seek to ~「〜しようとする」"},
    {"no": 435, "word": "step down", "pos": "動詞", "meaning": "辞任する(身を引く)", "example_en": "Ms. Garcia will step down from her post in December.", "example_ja": "ガルシアさんは今の職を12月に辞める。", "notes": "同: resign「辞任する」"},
    {"no": 436, "word": "technique", "pos": "名詞", "meaning": "手法", "example_en": "The agency uses various advertising techniques.", "example_ja": "その代理店はさまざまな広告手法を使う。", "notes": "「技術、技能」という意味もある。形: technical「技術上の、専門的な」、副: technically「技術的に、厳密にいえば」、名: technician「技術者」(=engineer「技術者」)"},
    {"no": 437, "word": "temporary", "pos": "形容詞", "meaning": "臨時の", "example_en": "I found a temporary job at a department store.", "example_ja": "私はデパートでの臨時の仕事を見つけた。", "notes": "「一時的な」という意味もある。反: permanent「恒久的な」、副: temporarily「一時的に」"},
    {"no": 438, "word": "factor", "pos": "名詞", "meaning": "要因", "example_en": "What's the most important factor in choosing a job?", "example_ja": "仕事を選ぶ際、最も重要な要因は何ですか。", "notes": "同: element「要因」、deciding factor「決定的な要因」"},
    {"no": 439, "word": "assemble", "pos": "動詞", "meaning": "組み立てる", "example_en": "These computers were assembled in Taiwan.", "example_ja": "これらのコンピュータは台湾で組み立てられた。", "notes": "「（人が）集まる」という意味もある。名: assembly「組み立て、集会、議会」、assembly line「（工場の）組み立てライン」"},
    {"no": 440, "word": "attention", "pos": "名詞", "meaning": "注意", "example_en": "I wasn't paying attention to him.", "example_ja": "私は彼に注意を払っていなかった。", "notes": "pay attention to ~「〜に注意を払う」、形: attentive「よく注意している、心づかいの行き届いた」"},
    {"no": 441, "word": "invoice", "pos": "名詞", "meaning": "請求書", "example_en": "We've received an invoice for sixty-five dollars.", "example_ja": "私たちは65ドルの請求書を受け取った。", "notes": "同: bill「請求書」"},
    {"no": 442, "word": "prior to", "pos": "前置詞", "meaning": "〜の前に", "example_en": "Please arrive fifteen minutes prior to your appointment.", "example_ja": "予約時間の15分前に到着するようにしてください。", "notes": "同: before「〜の前に」、形: prior「事前の」"},
    {"no": 443, "word": "refreshment", "pos": "名詞", "meaning": "軽い飲食料", "example_en": "Refreshments will be served after the meeting.", "example_ja": "会議の後、軽い飲食料が出ます。", "notes": "動: refresh「すっきりさせる」、形: refreshing「さわやかな」、名: beverage「飲み物」"},
    {"no": 444, "word": "trust", "pos": "名詞", "meaning": "信用", "example_en": "Honesty is the key to building trust.", "example_ja": "誠実さは信用を築く鍵である。", "notes": "「信託」という意味もある。動: trust「信用する、当てにする」、形: trustworthy「信用できる、当てにできる」"},
    {"no": 445, "word": "plumber", "pos": "名詞", "meaning": "配管工", "example_en": "I called the plumber to fix the sink.", "example_ja": "流しを修理するために配管工に電話した。", "notes": "名: plumbing「配管」"},
    {"no": 446, "word": "update", "pos": "動詞", "meaning": "更新する", "example_en": "We update our Web site daily.", "example_ja": "私たちは毎日ウェブサイトを更新する。", "notes": "「最新の情報を与える、新しいものに替える」という意味もある。名: update「最新情報」"},
    {"no": 447, "word": "upstairs", "pos": "副詞", "meaning": "上の階に", "example_en": "We have a meeting room upstairs.", "example_ja": "上の階に会議用の部屋があります。", "notes": "形: upstairs「上の階の」、名: upstairs「上の階」、反: downstairs「下の階に」、名: stairs「階段」"},
    {"no": 448, "word": "manner", "pos": "名詞", "meaning": "態度", "example_en": "Matt acted in a professional manner.", "example_ja": "マットはプロらしい態度で行動した。", "notes": "「やり方、礼儀作法（この意味では複数形mannersになる）」などの意味もある。in a calm manner「落ち着いた態度で」"},
    {"no": 449, "word": "consider", "pos": "動詞", "meaning": "考える", "example_en": "I'm considering taking the course.", "example_ja": "私はそのコースを取ろうかどうか考えている。", "notes": "consider ~ing「〜することを考える」、名: consideration「考慮、思いやり」、形: considerable「かなりの」、副: considerably「かなり」(=significantly, substantially)"},
    {"no": 450, "word": "executive", "pos": "名詞", "meaning": "重役", "example_en": "Ms. James is an executive of a computer company.", "example_ja": "ジェームズさんはコンピュータ会社の重役です。", "notes": "形: executive「経営に関する、重役の」、chief executive officer (略: CEO)「最高経営責任者」"},
    {"no": 451, "word": "means", "pos": "名詞", "meaning": "手段", "example_en": "Do you have any means of identification?", "example_ja": "身元を証明する手段を何かお持ちですか。", "notes": "meansは単数形でもsが付く。by all means「いかなる犠牲を払っても」"},
    {"no": 452, "word": "regarding", "pos": "前置詞", "meaning": "〜に関する", "example_en": "We have received your letter regarding the defective products.", "example_ja": "当社は欠陥商品に関するあなたからの手紙を受け取りました。", "notes": "同: about, concerning, with regard to「〜に関する」、動: regard「〜と見なす」、名: regard「尊敬、関心」"},
    {"no": 453, "word": "association", "pos": "名詞", "meaning": "提携", "example_en": "The book was published in association with the National Museum.", "example_ja": "この本は国立博物館の協力によって出版された。", "notes": "「関連、協会、連想」などの意味もある。in association with ~「〜と協力して(=in cooperation with)」、動: associate「関連付ける」、名: associate「仲間、共同経営者」"},
    {"no": 454, "word": "budget", "pos": "名詞", "meaning": "予算", "example_en": "They're reviewing the budget for next year.", "example_ja": "彼らは来年度の予算案を検討している。", "notes": "動: budget「割り当てる」、形: budget「低価格の」(=cheap, inexpensive, affordable, reasonable)"},
    {"no": 455, "word": "contain", "pos": "動詞", "meaning": "含む", "example_en": "This report contains information about the company's financial condition.", "example_ja": "この報告書には会社の財政状況に関する情報が含まれています。", "notes": "「中に入っている」という意味もある。名: container「容器」"},
    {"no": 456, "word": "remain", "pos": "動詞", "meaning": "〜のままでいる", "example_en": "Please remain seated during take-off.", "example_ja": "離陸の際、座ったままでいてください。", "notes": "「とどまる」(=stay)という意味もある。名: remainder「残り」(=rest)"},
    {"no": 457, "word": "chemical", "pos": "名詞", "meaning": "化学薬品", "example_en": "We use dangerous chemicals in our plant.", "example_ja": "当社の工場では危険な化学薬品を使っている。", "notes": "agricultural chemical「農薬」、形: chemical「化学の、化学的な」、名: chemistry「化学」、名: chemist「化学者」"},
    {"no": 458, "word": "demonstrate", "pos": "動詞", "meaning": "実地説明をする", "example_en": "I'll be demonstrating some of our new products.", "example_ja": "当社の新製品のいくつかを取り出して実地説明いたします。", "notes": "「証明する、はっきりと示す」という意味もある。名: demonstration「デモンストレーション、実演」"},
    {"no": 459, "word": "qualified", "pos": "形容詞", "meaning": "適任である", "example_en": "Tom is qualified for the position.", "example_ja": "トムはその職に適任である。", "notes": "「資格を持っている」という意味もある。動: qualify「資格を得る、資格を持つ、資格を与える」、名: qualification「資格、適任」"},
    {"no": 460, "word": "revise", "pos": "動詞", "meaning": "修正する", "example_en": "We have to revise the budget.", "example_ja": "私たちは予算を修正する必要がある。", "notes": "「改訂する、復習する」という意味もある。名: revision「変更、見直し」"},
    {"no": 461, "word": "relaxed", "pos": "形容詞", "meaning": "くつろいだ", "example_en": "When she entered the room, she looked relaxed.", "example_ja": "彼女は部屋に入ってきたとき、くつろいだように見えた。", "notes": "動: relax「リラックスする」、名: relaxation「くつろぎ、緩和」"},
    {"no": 462, "word": "upgrade", "pos": "動詞", "meaning": "改良する", "example_en": "We can't afford to upgrade our facilities.", "example_ja": "私たちは設備を改良する余裕がない。", "notes": "「向上させる、格上げする、アップグレードする」などの意味もある。名: upgrade「改良、アップグレード」"},
    {"no": 463, "word": "accompany", "pos": "動詞", "meaning": "同行する", "example_en": "Betty will accompany me to the conference.", "example_ja": "ベティーは私に同行して会議に行く。", "notes": "同: go with ~「〜と一緒に行く」"},
    {"no": 464, "word": "attitude", "pos": "名詞", "meaning": "態度(姿勢)", "example_en": "He has a positive attitude to his work.", "example_ja": "彼は自分の仕事に対して積極的な態度を取っている。", "notes": "「見方、姿勢」という意味もある。後ろに続く前置詞はtoまたはtoward(s)"},
    {"no": 465, "word": "commute", "pos": "動詞", "meaning": "通勤する", "example_en": "Amanda commutes to Montreal every day.", "example_ja": "アマンダは毎日モントリオールに通っている。", "notes": "名: commute「通勤、通学」、名: commuter「通う人」、commuter train「通勤列車」"},
    {"no": 466, "word": "competitive", "pos": "形容詞", "meaning": "競争力のある", "example_en": "We need to cut labor costs to stay competitive.", "example_ja": "私たちは競争力を保つため、人件費を削減する必要がある。", "notes": "「競争が激しい、競争心の強い、他に負けない」という意味もある。動: compete「競う」、名: competition「競争」、名: competitor「競争相手、ライバル」"},
    {"no": 467, "word": "refuse", "pos": "動詞", "meaning": "拒否する", "example_en": "He refused to speak with journalists.", "example_ja": "彼は報道関係者と話をすることを拒絶した。", "notes": "「（申し出などを）断る」という意味もある。反: accept「受け入れる」、名: refusal「拒否」"},
    {"no": 468, "word": "subscribe", "pos": "動詞", "meaning": "定期購読する", "example_en": "I subscribe to Business Weekly.", "example_ja": "私はビジネスウィークリーを定期購読している。", "notes": "後ろに続く前置詞はto。名: subscription「定期購読」、名: subscriber「定期購読者」"},
    {"no": 469, "word": "process", "pos": "動詞", "meaning": "処理する", "example_en": "It will take two weeks to process your visa application.", "example_ja": "あなたのビザ申請を処理するのに2週間かかります。", "notes": "「加工する」という意味もある。名: process「過程、作用、進行」、形: processed「加工された」"},
    {"no": 470, "word": "comment", "pos": "名詞", "meaning": "意見", "example_en": "He made helpful comments on my proposal.", "example_ja": "彼は私の企画書に有益な意見を出してくれた。", "notes": "動: comment「意見を述べる」。名詞・動詞ともに後ろに前置詞onが続く"},
    {"no": 471, "word": "necessary", "pos": "形容詞", "meaning": "必要な", "example_en": "Is it necessary to fill out this form?", "example_ja": "この用紙に記入する必要がありますか。", "notes": "「必然的な」という意味もある。同: essential, vital「絶対必要な」、名: necessity「必要、必需品」"},
    {"no": 472, "word": "respectively", "pos": "副詞", "meaning": "それぞれ", "example_en": "Auckland and Sydney were ranked fifth and tenth, respectively.", "example_ja": "オークランドとシドニーはそれぞれ5位と10位にランク付けされた。", "notes": "形: respective「それぞれの」、関: in respect of ~「〜に関して」"},
    {"no": 473, "word": "probable", "pos": "形容詞", "meaning": "起こりそうな", "example_en": "It is probable that unemployment will rise further.", "example_ja": "失業率はさらに上がる見込みだ。", "notes": "同: likely「起こりそうな」、関: possible「可能性がある」（probableより可能性が低い）、名: probability「見込み」(=likelihood)、副: probably「多分、おそらく」"},
    {"no": 474, "word": "efficient", "pos": "形容詞", "meaning": "効率のよい", "example_en": "We need more efficient methods of collecting data.", "example_ja": "私たちはもっと効率のよいデータ収集方法が必要です。", "notes": "「有能な」という意味もある。energy efficient「燃費のよい」、名: efficiency「効率」、副: efficiently「効率的に」"},
    {"no": 475, "word": "identify", "pos": "動詞", "meaning": "明らかにする", "example_en": "First, we must identify problem areas.", "example_ja": "はじめに私たちは問題点を明らかにしなければならない。", "notes": "「身元を確認する」という意味もある。名: identification「身分証明」"},
    {"no": 476, "word": "particular", "pos": "形容詞", "meaning": "特定の", "example_en": "Is there any particular movie you want to see?", "example_ja": "何か特に見たい映画はありますか。", "notes": "同: specific, certain「特定の」、副: particularly「特に」"},
    {"no": 477, "word": "relocate", "pos": "動詞", "meaning": "移転する", "example_en": "The company relocated to Los Angeles.", "example_ja": "その会社はロサンゼルスに移転した。", "notes": "relocate to 〈地名〉「〜へ移転する」、同: move to「〜へ引っ越す」、名: relocation「移転」"},
    {"no": 478, "word": "remind", "pos": "動詞", "meaning": "思い出させる", "example_en": "My secretary reminded me about the meeting tomorrow.", "example_ja": "秘書が私に明日の会議のことを思い出させてくれた。", "notes": "関: remember「覚えている」、名: reminder「思い出させるもの」"},
    {"no": 479, "word": "compared with", "pos": "熟語", "meaning": "〜と比べて", "example_en": "Our sales rose ten percent compared with last year.", "example_ja": "当社の売り上げは昨年と比べ、10パーセント上がった。", "notes": "compared to でも同じ意味になる。名: comparison「比較」"},
    {"no": 480, "word": "establish", "pos": "動詞", "meaning": "設立する", "example_en": "The company was established in 1967.", "example_ja": "その会社は1967年に設立された。", "notes": "「確立する、証明する、認めるせる」などの意味もある。同: found「設立する」、名: establishment「設立、機関、権力層」、形: established「すでにある、定評のある」"},
    {"no": 481, "word": "point out", "pos": "句動詞", "meaning": "指摘する", "example_en": "He pointed out that these data are inaccurate.", "example_ja": "彼はこれらのデータが正確でないことを指摘した。", "notes": "point out A to ~「〜にAを指摘する」"},
    {"no": 482, "word": "property", "pos": "名詞", "meaning": "不動産", "example_en": "Property prices are falling this month.", "example_ja": "今月、不動産の価格は下がっている。", "notes": "「財産、所有物、特性」などの意味もある。"},
    {"no": 483, "word": "restore", "pos": "動詞", "meaning": "修復する", "example_en": "The building was restored after the fire.", "example_ja": "その建物は火事のあと、修復された。", "notes": "「元の状態に戻す」という意味がある。名: restoration「復元、回復、復興、返還」"},
    {"no": 484, "word": "status", "pos": "名詞", "meaning": "状況", "example_en": "What's the status of our order?", "example_ja": "私たちの注文品の状況はどうなっていますか。", "notes": "「地位」という意味もある。status quo「現状」"},
    {"no": 485, "word": "expense", "pos": "名詞", "meaning": "経費", "example_en": "The company will cover travel expenses.", "example_ja": "会社が旅費を出してくれます。", "notes": "関: expenditure「支出」、形: expensive「高価な」(=costly, pricey)"},
    {"no": 486, "word": "focus", "pos": "動詞", "meaning": "焦点を合わせる", "example_en": "The conference focuses on environmental issues.", "example_ja": "その会議は環境問題に焦点を合わせている。", "notes": "焦点を合わせる対象は前置詞onによって導く。「集中させる」という意味もある。名: focus「焦点、中心」"},
    {"no": 487, "word": "laboratory", "pos": "名詞", "meaning": "研究所", "example_en": "The company has a research laboratory in Miami.", "example_ja": "その会社はマイアミに研究所を持っている。", "notes": "「実験室」という意味にもなる。略: lab"},
    {"no": 488, "word": "obtain", "pos": "動詞", "meaning": "得る", "example_en": "You must obtain permission from the publisher.", "example_ja": "あなたは出版社から許可を得なければなりません。", "notes": "同: get「得る」、形: obtainable「手に入れることができる」"},
    {"no": 489, "word": "reputation", "pos": "名詞", "meaning": "評判", "example_en": "We have a reputation for quality.", "example_ja": "当社は品質の良さで評判を得ている。", "notes": "形: reputed「〜といわれている」"},
    {"no": 490, "word": "retail", "pos": "名詞", "meaning": "小売り", "example_en": "You can buy these products at retail stores.", "example_ja": "これらの製品は小売店でご購入いただけます。", "notes": "関: wholesale「卸売り」、名: retailer「小売業者」、関: wholesaler「卸売り業者」"},
    {"no": 491, "word": "contribute", "pos": "動詞", "meaning": "寄付する", "example_en": "Ms. Hunter contributed ten thousand dollars to the school.", "example_ja": "ハンターさんはその学校へ1万ドルの寄付をした。", "notes": "「貢献する、原因となる、寄稿する」という意味もある。toとセットで使われることが多い。名: contribution「寄付、貢献、寄稿」"},
    {"no": 492, "word": "convince", "pos": "動詞", "meaning": "納得させる", "example_en": "We have to convince the president.", "example_ja": "私たちは社長を納得させなければならない。", "notes": "形: convinced「確信した」、形: convincing「説得力のある」(=persuasive)"},
    {"no": 493, "word": "divide", "pos": "動詞", "meaning": "分ける", "example_en": "We should divide the profits equally among us.", "example_ja": "利益は私たちの間で平等に分けるべきです。", "notes": "「隔てる、割り算をする」などの意味もある。同: share「分ける」、名: division「部署(=department)、分包、区画」"},
    {"no": 494, "word": "fine", "pos": "名詞", "meaning": "罰金", "example_en": "I got a 55-dollar fine for illegal parking.", "example_ja": "私は違法駐車で55ドルの罰金を取られた。", "notes": "動: fine「罰金を科す」。形容詞のfine（よい、優れた、晴れたなどの意）とはまったく別の意味"},
    {"no": 495, "word": "inquire", "pos": "動詞", "meaning": "尋ねる", "example_en": "I inquired about their service.", "example_ja": "私は彼らのサービスについて尋ねた。", "notes": "enquireという綴りもある（主に英）。名: inquiry「問い合わせ」、make an inquiry「問い合わせる」"},
    {"no": 496, "word": "specific", "pos": "形容詞", "meaning": "明確な・特定の", "example_en": "Each product is designed for a specific purpose.", "example_ja": "それぞれの製品は特定の目的のために作られています。", "notes": "「厳密な」という意味もある。同: particular, certain「特定の」、副: specifically「特に、厳密に」、名: specification「仕様書」"},
    {"no": 497, "word": "stock", "pos": "名詞", "meaning": "在庫", "example_en": "This model is currently out of stock.", "example_ja": "このモデルは現在、在庫が切れています。", "notes": "「株式」という意味もある。同: inventory「在庫」、in stock「在庫がある」、out of stock「在庫がない」、動: stock「仕入れる、満たす」"},
    {"no": 498, "word": "aware", "pos": "形容詞", "meaning": "気が付いている", "example_en": "We are aware that our sales network is insufficient.", "example_ja": "私たちは販売網が十分でないことを知っています。", "notes": "aware of ~「〜に気付いている」、名: awareness「認識、自覚」"},
    {"no": 499, "word": "broad", "pos": "形容詞", "meaning": "大まかな", "example_en": "He gave us a broad outline of the plan.", "example_ja": "彼は私たちにその計画の大まかな概要を示した。", "notes": "「広い」という意味もある。動: broaden「広げる」(=widen, expand)"},
    {"no": 500, "word": "maximum", "pos": "形容詞", "meaning": "最大の", "example_en": "The factory is operating at maximum capacity.", "example_ja": "その工場は稼働能力限界で操業している。", "notes": "反: minimum「最小の」、動: maximize「最大にする」、反: minimize「最小限にする」、名: maximum「最大限」(反: minimum「最小限」)"}
]

CHOICE_LABELS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

quiz_en_ja = []
quiz_ja_en = []

for idx, item in enumerate(words_data):
    w_no = item["no"]
    w_word = item["word"]
    w_pos = item["pos"]
    w_meaning = item["meaning"]
    
    # --- 英→日 ---
    other_meanings = [x["meaning"] for x in words_data if x["meaning"] != w_meaning and x["no"] != w_no]
    dummy_meanings = random.sample(other_meanings, 9)
    choices_meaning = [w_meaning] + dummy_meanings
    random.shuffle(choices_meaning)
    correct_choice_letter_meaning = CHOICE_LABELS[choices_meaning.index(w_meaning)]
    
    quiz_en_ja.append({
        "q_no": idx + 1,
        "no": w_no,
        "word": w_word,
        "pos": w_pos,
        "meaning": w_meaning,
        "choices": choices_meaning,
        "correct_letter": correct_choice_letter_meaning,
        "example_en": item["example_en"],
        "example_ja": item["example_ja"],
        "notes": item["notes"]
    })
    
    # --- 日→英 ---
    other_words = [x["word"] for x in words_data if x["word"] != w_word and x["no"] != w_no]
    dummy_words = random.sample(other_words, 9)
    choices_word = [w_word] + dummy_words
    random.shuffle(choices_word)
    correct_choice_letter_word = CHOICE_LABELS[choices_word.index(w_word)]
    
    quiz_ja_en.append({
        "q_no": idx + 1,
        "no": w_no,
        "word": w_word,
        "pos": w_pos,
        "meaning": w_meaning,
        "choices": choices_word,
        "correct_letter": correct_choice_letter_word,
        "example_en": item["example_en"],
        "example_ja": item["example_ja"],
        "notes": item["notes"]
    })

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
ws_words = wb.create_sheet(title="単語帳一覧(401-500)")
ws_words.views.sheetView[0].showGridLines = True
ws_words.freeze_panes = "A5"

ws_words.merge_cells("A1:G1")
ws_words["A1"] = "TOEIC L&R 出る単特急 金のフレーズ 重要単語一覧 (No. 401 - 500)"
ws_words["A1"].font = Font(name=font_family, size=15, bold=True, color="FFFFFF")
ws_words["A1"].fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
ws_words["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws_words.row_dimensions[1].height = 36

ws_words.merge_cells("A2:G2")
ws_words["A2"] = "収録語数: 全100語 | 出題範囲: 401〜500 | 例文・和訳・重要ポイント付き"
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
    ws["C2"].font = Font(name=font_family, size=9, bold=True, color="15803D")
    ws["C2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("C3:D3")
    ws["C3"] = '=COUNTIF(P6:P105, "○ 正解")'
    ws["C3"].font = Font(name=font_family, size=13, bold=True, color="15803D")
    ws["C3"].alignment = Alignment(horizontal="center", vertical="center")
    
    # 不正解数
    ws.merge_cells("E2:F2")
    ws["E2"] = "不正解数"
    ws["E2"].font = Font(name=font_family, size=9, bold=True, color="B91C1C")
    ws["E2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("E3:F3")
    ws["E3"] = '=COUNTIF(P6:P105, "× 不正解")'
    ws["E3"].font = Font(name=font_family, size=13, bold=True, color="B91C1C")
    ws["E3"].alignment = Alignment(horizontal="center", vertical="center")
    
    # 正答率
    ws.merge_cells("G2:H2")
    ws["G2"] = "正答率"
    ws["G2"].font = Font(name=font_family, size=9, bold=True, color="1D4ED8")
    ws["G2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("G3:H3")
    ws["G3"] = '=IF(COUNTA(O6:O105)>0, COUNTIF(P6:P105, "○ 正解")/COUNTA(O6:O105), 0)'
    ws["G3"].number_format = '0.0%'
    ws["G3"].font = Font(name=font_family, size=13, bold=True, color="1D4ED8")
    ws["G3"].alignment = Alignment(horizontal="center", vertical="center")
    
    # 使い方
    ws.merge_cells("I2:T3")
    ws["I2"] = "【使い方】出題の順番は単語番号順(401〜500)です。O列「あなたの回答」でドロップダウン(A〜J)を選択すると自動判定されます。\n正解判定後に右側の解答・解説（Q〜T列）を確認して復習しましょう！"
    ws["I2"].font = Font(name=font_family, size=9, color="334155")
    ws["I2"].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    
    ws.row_dimensions[4].height = 8
    ws.row_dimensions[5].height = 28
    
    quiz_headers = [
        ("問", "1E3A8A"),
        ("単語No.", "1E3A8A"),
        ("出題 (" + ("英単語" if is_en_to_ja else "日本語の意味") + ")", "1E3A8A"),
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
    main_title="TOEIC L&R 100問10択クイズ 【英単語 → 日本語の意味】 (出題順: 401〜500)",
    quiz_data=quiz_en_ja,
    is_en_to_ja=True
)

build_quiz_sheet(
    sheet_title="10択クイズ(日→英)",
    main_title="TOEIC L&R 100問10択クイズ 【日本語の意味 → 英単語】 (出題順: 401〜500)",
    quiz_data=quiz_ja_en,
    is_en_to_ja=False
)

excel_path = os.path.join(OUTPUT_DIR, "TOEIC_Words_401-500_100Quiz.xlsx")
try:
    wb.save(excel_path)
    print("Saved Excel:", excel_path)
except PermissionError:
    print(f"Notice: {excel_path} is open in Excel, skipped rewrite.")

excel_path_ja = os.path.join(OUTPUT_DIR, "TOEIC単語401-500_100問10択クイズ.xlsx")
try:
    import shutil
    shutil.copyfile(excel_path, excel_path_ja)
    print("Saved Excel (JA):", excel_path_ja)
except Exception as e:
    print("Could not copy JA Excel:", e)

# -------------------------------------------------------------
# 2. CSV 作成 (UTF-8 with BOM)
# -------------------------------------------------------------
csv_words_file = os.path.join(OUTPUT_DIR, "TOEIC_Words_401-500_List.csv")
try:
    with open(csv_words_file, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["No.", "英単語", "日本語訳", "品詞", "例文", "例文の日本語訳", "補足・関連語"])
        for w in words_data:
            writer.writerow([w["no"], w["word"], w["meaning"], w["pos"], w["example_en"], w["example_ja"], w["notes"]])
except PermissionError:
    print(f"Notice: {csv_words_file} is open in Excel, skipped rewrite.")

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

print("Saved CSV files.")

# 日本語名でのコピーも作成
try:
    shutil.copyfile(csv_words_file, os.path.join(OUTPUT_DIR, "TOEIC単語一覧_401-500.csv"))
    shutil.copyfile(csv_quiz_en_file, os.path.join(OUTPUT_DIR, "TOEIC_100問10択クイズ_英日.csv"))
    shutil.copyfile(csv_quiz_ja_file, os.path.join(OUTPUT_DIR, "TOEIC_100問10択クイズ_日英.csv"))
except Exception as e:
    pass

# -------------------------------------------------------------
# 3. HTML インタラクティブ学習アプリ 作成
# -------------------------------------------------------------
quiz_data_json = json.dumps({
    "en_ja": quiz_en_ja,
    "ja_en": quiz_ja_en,
    "all_words": words_data
}, ensure_ascii=False, indent=2)

html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TOEIC 100問10択クイズ (No.401-500)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #eff6ff;
      --success: #16a34a;
      --success-light: #dcfce7;
      --danger: #dc2626;
      --danger-light: #fee2e2;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', 'Noto Sans JP', sans-serif;
    }}

    body {{
      background: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 1.5rem 1rem;
    }}

    .container {{
      max-width: 860px;
      margin: 0 auto;
      width: 100%;
    }}

    header {{
      background: var(--card-bg);
      padding: 1.25rem 1.5rem;
      border-radius: 1rem;
      box-shadow: var(--shadow);
      margin-bottom: 1.25rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      border: 1px solid var(--border);
    }}

    .title-group h1 {{
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .title-group p {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    .controls {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    select, button.control-btn {{
      padding: 0.5rem 0.85rem;
      border-radius: 0.5rem;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-main);
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    select:focus, button.control-btn:focus {{
      outline: 2px solid var(--primary);
    }}

    button.control-btn:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    .dashboard {{
      background: var(--card-bg);
      border-radius: 1rem;
      padding: 1rem 1.5rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}

    .stats-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.9rem;
      font-weight: 600;
    }}

    .stat-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.25rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.8rem;
    }}

    .badge-correct {{ background: var(--success-light); color: var(--success); }}
    .badge-wrong {{ background: var(--danger-light); color: var(--danger); }}
    .badge-accuracy {{ background: var(--primary-light); color: var(--primary); }}

    .progress-bar-bg {{
      height: 8px;
      background: var(--border);
      border-radius: 9999px;
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary), #3b82f6);
      width: 1%;
      transition: width 0.3s ease;
    }}

    .quiz-card {{
      background: var(--card-bg);
      border-radius: 1.25rem;
      padding: 2rem 1.75rem;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--border);
      position: relative;
    }}

    .question-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }}

    .q-number {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-light);
      padding: 0.35rem 0.8rem;
      border-radius: 0.5rem;
    }}

    .pos-tag {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #475569;
      background: #f1f5f9;
      padding: 0.35rem 0.75rem;
      border-radius: 0.5rem;
    }}

    .target-wrapper {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      margin: 1.25rem 0 1.75rem 0;
    }}

    .target-word {{
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--text-main);
      text-align: center;
      letter-spacing: -0.02em;
    }}

    .btn-audio {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      padding: 0.35rem 0.85rem;
      height: 36px;
      border-radius: 18px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--primary);
      transition: all 0.2s;
    }}

    .btn-audio:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    .choices-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .choices-grid {{
        grid-template-columns: 1fr;
      }}
      .target-word {{
        font-size: 1.75rem;
      }}
    }}

    .choice-btn {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: #ffffff;
      border: 2px solid var(--border);
      padding: 0.85rem 1rem;
      border-radius: 0.75rem;
      cursor: pointer;
      font-size: 0.95rem;
      font-weight: 500;
      text-align: left;
      transition: all 0.15s ease;
      color: var(--text-main);
      position: relative;
    }}

    .choice-btn:hover:not(:disabled) {{
      border-color: var(--primary);
      background: var(--primary-light);
      transform: translateY(-1px);
    }}

    .choice-key {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      background: #f1f5f9;
      color: #475569;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
    }}

    .choice-btn.correct {{
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: var(--success) !important;
      font-weight: 700;
    }}
    .choice-btn.correct .choice-key {{
      background: var(--success);
      color: #fff;
    }}

    .choice-btn.wrong {{
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: var(--danger) !important;
    }}
    .choice-btn.wrong .choice-key {{
      background: var(--danger);
      color: #fff;
    }}

    .explanation-card {{
      background: #f8fafc;
      border-left: 4px solid var(--primary);
      padding: 1.25rem;
      border-radius: 0.5rem;
      margin-top: 1rem;
      display: none;
      animation: fadeIn 0.25s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .explanation-title {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .example-en-row {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.25rem;
    }}

    .example-en {{
      font-size: 1rem;
      font-weight: 600;
      color: #1e293b;
    }}

    .btn-audio-sm {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--primary);
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .btn-audio-sm:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    .example-ja {{
      font-size: 0.9rem;
      color: #64748b;
      margin-bottom: 0.5rem;
    }}

    .notes-text {{
      font-size: 0.85rem;
      background: #f1f5f9;
      padding: 0.5rem 0.75rem;
      border-radius: 0.4rem;
      color: #334155;
    }}

    .action-row {{
      display: flex;
      justify-content: flex-end;
      align-items: center;
      margin-top: 1.5rem;
      gap: 0.75rem;
    }}

    .btn-next {{
      background: var(--primary);
      color: #ffffff;
      padding: 0.75rem 2rem;
      font-size: 1rem;
      font-weight: 700;
      border: none;
      border-radius: 0.75rem;
      cursor: pointer;
      display: none;
      transition: background 0.2s;
    }}

    .btn-next:hover {{
      background: var(--primary-dark);
    }}

    .result-view {{
      display: none;
      text-align: center;
      padding: 3rem 1.5rem;
    }}

    .result-score {{
      font-size: 4rem;
      font-weight: 800;
      color: var(--primary);
      margin: 1rem 0;
    }}

    .result-actions {{
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-top: 2rem;
    }}
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="title-group">
        <h1>TOEIC 100問10択クイズ</h1>
        <p>No. 401 〜 500 (出題順: 番号順)</p>
      </div>
      <div class="controls">
        <select id="modeSelect" onchange="changeMode()">
          <option value="en_ja">英単語 → 日本語の意味 (10択)</option>
          <option value="ja_en">日本語の意味 → 英単語 (10択)</option>
        </select>
        <button class="control-btn" onclick="resetQuiz()">最初から解く</button>
      </div>
    </header>

    <div class="dashboard" id="dashboard">
      <div class="stats-row">
        <div>
          <span>進捗: </span>
          <span id="progressText" style="font-weight: 700;">1 / 100</span>
        </div>
        <div style="display: flex; gap: 0.5rem;">
          <span class="stat-badge badge-correct">○ <span id="correctCount">0</span></span>
          <span class="stat-badge badge-wrong">× <span id="wrongCount">0</span></span>
          <span class="stat-badge badge-accuracy">正答率: <span id="accuracyText">0.0%</span></span>
        </div>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="progressBar"></div>
      </div>
    </div>

    <div class="quiz-card" id="quizCard">
      <div class="question-header">
        <span class="q-number" id="qNumberBadge">Q1 / 100 [No. 401]</span>
        <span class="pos-tag" id="posTag">動詞</span>
      </div>

      <div class="target-wrapper">
        <div class="target-word" id="targetWord">cause</div>
        <button class="btn-audio" id="btnSpeakWord" title="単語の発音を聞く" onclick="speakTargetWord()">発音</button>
      </div>

      <div class="choices-grid" id="choicesGrid"></div>

      <div class="explanation-card" id="explanationCard">
        <div class="explanation-title">単語解説・例文</div>
        <div class="example-en-row">
          <div class="example-en" id="expEn">Heavy traffic is causing delays on Highway 18.</div>
          <button class="btn-audio-sm" id="btnSpeakSentence" title="例文の発音を聞く" onclick="speakSentence()">例文音声</button>
        </div>
        <div class="example-ja" id="expJa">18号線では交通渋滞により遅れが生じています。</div>
        <div class="notes-text" id="expNotes">名: cause「原因、理由、大義」</div>
      </div>

      <div class="action-row">
        <button class="btn-next" id="btnNext" onclick="nextQuestion()">次の問題へ (Enter)</button>
      </div>
    </div>

    <div class="quiz-card result-view" id="resultView">
      <h2>お疲れ様でした！クイズ終了</h2>
      <p style="color: var(--text-muted); margin-top: 0.5rem;">100問の挑戦が完了しました！</p>
      
      <div class="result-score" id="finalScore">95 / 100</div>
      <p id="finalAccuracy" style="font-size: 1.25rem; font-weight: 600; color: #334155;">正答率: 95.0%</p>

      <div class="result-actions">
        <button class="btn-next" style="display: inline-block;" onclick="retryWrongOnly()" id="btnRetryWrong">間違えた問題のみ復習</button>
        <button class="control-btn" style="padding: 0.75rem 1.5rem;" onclick="resetQuiz()">もう一度最初から</button>
      </div>
    </div>
  </div>

  <script>
    const QUIZ_SOURCE = {quiz_data_json};
    const CHOICE_KEYS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];

    let currentMode = "en_ja";
    let questionsList = [];
    let currentIndex = 0;
    let correctTotal = 0;
    let wrongTotal = 0;
    let wrongQuestions = [];
    let isAnswered = false;

    function init() {{
      questionsList = [...QUIZ_SOURCE[currentMode]];
      currentIndex = 0;
      correctTotal = 0;
      wrongTotal = 0;
      wrongQuestions = [];
      isAnswered = false;
      
      document.getElementById("quizCard").style.display = "block";
      document.getElementById("resultView").style.display = "none";
      
      renderQuestion();
    }}

    function changeMode() {{
      currentMode = document.getElementById("modeSelect").value;
      init();
    }}

    function resetQuiz() {{
      init();
    }}

    function renderQuestion() {{
      isAnswered = false;
      const q = questionsList[currentIndex];
      
      document.getElementById("progressText").textContent = `${{currentIndex + 1}} / ${{questionsList.length}}`;
      document.getElementById("qNumberBadge").textContent = `Q${{q.q_no}} [No. ${{q.no}}]`;
      document.getElementById("posTag").textContent = q.pos;
      
      const pct = ((currentIndex) / questionsList.length) * 100;
      document.getElementById("progressBar").style.width = `${{Math.max(pct, 2)}}%`;
      
      const target = currentMode === "en_ja" ? q.word : q.meaning;
      document.getElementById("targetWord").textContent = target;

      const audioBtn = document.getElementById("btnSpeakWord");
      if (currentMode === "en_ja") {{
        audioBtn.style.display = "inline-flex";
      }} else {{
        audioBtn.style.display = "none";
      }}

      const grid = document.getElementById("choicesGrid");
      grid.innerHTML = "";
      
      q.choices.forEach((choice, idx) => {{
        const btn = document.createElement("button");
        btn.className = "choice-btn";
        btn.innerHTML = `<span class="choice-key">${{CHOICE_KEYS[idx]}}</span><span>${{choice}}</span>`;
        btn.onclick = () => handleAnswer(CHOICE_KEYS[idx], btn, q);
        grid.appendChild(btn);
      }});

      document.getElementById("explanationCard").style.display = "none";
      document.getElementById("btnNext").style.display = "none";
    }}

    function handleAnswer(selectedKey, clickedBtn, q) {{
      if (isAnswered) return;
      isAnswered = true;

      const isCorrect = (selectedKey === q.correct_letter);
      
      const allBtns = document.querySelectorAll(".choice-btn");
      allBtns.forEach((btn, idx) => {{
        btn.disabled = true;
        if (CHOICE_KEYS[idx] === q.correct_letter) {{
          btn.classList.add("correct");
        }}
      }});

      if (isCorrect) {{
        correctTotal++;
        document.getElementById("correctCount").textContent = correctTotal;
      }} else {{
        wrongTotal++;
        document.getElementById("wrongCount").textContent = wrongTotal;
        clickedBtn.classList.add("wrong");
        wrongQuestions.push(q);
      }}

      const answeredCount = correctTotal + wrongTotal;
      const acc = answeredCount > 0 ? ((correctTotal / answeredCount) * 100).toFixed(1) : "0.0";
      document.getElementById("accuracyText").textContent = `${{acc}}%`;

      document.getElementById("expEn").textContent = q.example_en;
      document.getElementById("expJa").textContent = q.example_ja;
      document.getElementById("expNotes").textContent = q.notes;
      document.getElementById("explanationCard").style.display = "block";

      const nextBtn = document.getElementById("btnNext");
      nextBtn.style.display = "inline-block";
      nextBtn.focus();
    }}

    function nextQuestion() {{
      currentIndex++;
      if (currentIndex < questionsList.length) {{
        renderQuestion();
      }} else {{
        showResult();
      }}
    }}

    function showResult() {{
      document.getElementById("quizCard").style.display = "none";
      const resView = document.getElementById("resultView");
      resView.style.display = "block";
      
      document.getElementById("progressBar").style.width = "100%";
      document.getElementById("progressText").textContent = `${{questionsList.length}} / ${{questionsList.length}}`;
      
      document.getElementById("finalScore").textContent = `${{correctTotal}} / ${{questionsList.length}}`;
      const acc = ((correctTotal / questionsList.length) * 100).toFixed(1);
      document.getElementById("finalAccuracy").textContent = `正答率: ${{acc}}%`;
      
      const btnRetry = document.getElementById("btnRetryWrong");
      if (wrongQuestions.length === 0) {{
        btnRetry.style.display = "none";
      }} else {{
        btnRetry.style.display = "inline-block";
        btnRetry.textContent = `間違えた${{wrongQuestions.length}}問のみ復習`;
      }}
    }}

    function retryWrongOnly() {{
      if (wrongQuestions.length === 0) return;
      questionsList = [...wrongQuestions];
      currentIndex = 0;
      correctTotal = 0;
      wrongTotal = 0;
      wrongQuestions = [];
      isAnswered = false;
      
      document.getElementById("correctCount").textContent = "0";
      document.getElementById("wrongCount").textContent = "0";
      document.getElementById("accuracyText").textContent = "0.0%";
      
      document.getElementById("quizCard").style.display = "block";
      document.getElementById("resultView").style.display = "none";
      
      renderQuestion();
    }}

    function speakText(text) {{
      if (!window.speechSynthesis) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = 0.9;
      window.speechSynthesis.speak(u);
    }}

    function speakTargetWord() {{
      const q = questionsList[currentIndex];
      speakText(q.word);
    }}

    function speakSentence() {{
      const q = questionsList[currentIndex];
      speakText(q.example_en);
    }}

    window.addEventListener("keydown", (e) => {{
      if (!isAnswered) {{
        const fullToHalf = {{'１':'1','２':'2','３':'3','４':'4','５':'5','６':'6','７':'7','８':'8','９':'9','０':'0'}};
        const normalizedKey = fullToHalf[e.key] || e.key;
        const index = CHOICE_KEYS.indexOf(normalizedKey);
        if (index !== -1) {{
          const btns = document.querySelectorAll(".choice-btn");
          if (btns[index]) {{
            btns[index].click();
          }}
        }}
      }} else {{
        if (e.key === "Enter" || e.key === " ") {{
          e.preventDefault();
          nextQuestion();
        }}
      }}
    }});

    init();
  </script>
</body>
</html>
'''

html_path = os.path.join(OUTPUT_DIR, "TOEIC_100Quiz_App.html")
with open(html_path, mode="w", encoding="utf-8") as f:
    f.write(html_content)
print("Saved HTML App:", html_path)

try:
    shutil.copyfile(html_path, os.path.join(OUTPUT_DIR, "TOEIC_100問10択クイズ_学習アプリ.html"))
except Exception as e:
    pass

print("=== All builds completed! ===")
