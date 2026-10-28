# -*- coding: utf-8 -*-
import random

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

CHOICE_LABELS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

quiz_en_ja = []
quiz_ja_en = []

for idx, item in enumerate(words_data):
    w_no = item["no"]
    w_word = item["word"]
    w_pos = item["pos"]
    w_meaning = item["meaning"]
    
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
