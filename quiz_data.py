# -*- coding: utf-8 -*-
import random

random.seed(2026)

words_data = [
    {'no': 501, 'word': 'aim', 'pos': '動詞', 'meaning': '向ける', 'example_en': 'Our campaign is aimed at young adults.', 'example_ja': '当社のキャンペーンはヤングアダルトに向けられている。', 'notes': '「目指す、目的とする」という意味もある（同: target「目標とする」） 名: aim「目的、目標」(=purpose, goal, target, objective)'},
    {'no': 502, 'word': 'cooperate', 'pos': '動詞', 'meaning': '協力する', 'example_en': 'The team members have to cooperate with each other.', 'example_ja': '部員はお互いに協力しなければならない。', 'notes': '名: cooperation「協力」、形: cooperative「協力的な」'},
    {'no': 503, 'word': 'quantity', 'pos': '名詞', 'meaning': '量', 'example_en': 'We get discounts when we buy materials in large quantities.', 'example_ja': '資材を大量に買うと割引が受けられる。', 'notes': '動: quantify「数値で表す」、形: quantitative「量的な」、反: quality「質」'},
    {'no': 504, 'word': 'by accident', 'pos': '熟語', 'meaning': '偶然に', 'example_en': 'We met at the conference by accident.', 'example_ja': '私たちは会議で偶然に会った。', 'notes': '反: deliberately, intentionally, on purpose「わざと」、名: accident「事故」、形: accidental「偶然の」、副: accidentally「偶然に」'},
    {'no': 505, 'word': 'launch', 'pos': '動詞', 'meaning': '始める', 'example_en': 'We launched an advertising campaign for our new products.', 'example_ja': '当社は新製品のための広告キャンペーンを開始した。', 'notes': '「発売を開始する」という意味も重要。名: launch「開始」'},
    {'no': 506, 'word': 'obvious', 'pos': '形容詞', 'meaning': '明らかな', 'example_en': 'It is obvious that the company is not doing well.', 'example_ja': '会社の業績がよくないことは明らかだ。', 'notes': '副: obviously「明らかに」'},
    {'no': 507, 'word': 'optimistic', 'pos': '形容詞', 'meaning': '楽観的な', 'example_en': "I'm optimistic about the company's future.", 'example_ja': '私は会社の将来について楽観的だ。', 'notes': '反: pessimistic「悲観的な」、名: optimist「楽観的な人」（反: pessimist「悲観的な人」）'},
    {'no': 508, 'word': 'owe', 'pos': '動詞', 'meaning': '〜のおかげである', 'example_en': 'I owe my success to my colleagues.', 'example_ja': '私の成功は同僚のおかげである。', 'notes': '「借りがある」という意味もある。owing to 〜「〜のおかげで」(=because of, due to, thanks to)'},
    {'no': 509, 'word': 'vision', 'pos': '名詞', 'meaning': '考え', 'example_en': 'The company needs a clear vision for the future.', 'example_ja': 'その会社は将来に対する明確な考えが必要である。', 'notes': '「視力、視界、展望」などの意味もある'},
    {'no': 510, 'word': 'withdraw', 'pos': '動詞', 'meaning': '引き出す', 'example_en': 'I just withdrew three hundred dollars from my account.', 'example_ja': '私は口座から300ドル下ろしたばかりです。', 'notes': '過去: withdrew、過去分詞: withdrawn「手を引く、撤退する、取り消す」という意味もある。名: withdrawal「（預金の）引き出し、撤退、撤回」'},
    {'no': 511, 'word': 'deliberately', 'pos': '副詞', 'meaning': 'わざと', 'example_en': 'I deliberately misplaced the folder.', 'example_ja': '私はわざとそのホルダーを違う場所に置いた。', 'notes': '同: intentionally, on purpose「わざと」、形: deliberate「故意の」(=intentional)、動: deliberate「熟考する」、名: deliberation「熟考」、after long deliberation「長い熟考のあと」'},
    {'no': 512, 'word': 'dismiss', 'pos': '動詞', 'meaning': '解雇する', 'example_en': 'She was unfairly dismissed from her post.', 'example_ja': '彼女は職を不当に解雇された。', 'notes': '同: fire「解雇する」、名: dismissal「解雇」'},
    {'no': 513, 'word': 'glance', 'pos': '動詞', 'meaning': 'さっと見る', 'example_en': "He's glancing at a magazine.", 'example_ja': '彼は雑誌にさっと目を通している。', 'notes': '後ろに続く前置詞はat。名: glance「さっと見ること」、at a glance「一見して」'},
    {'no': 514, 'word': 'ingredient', 'pos': '名詞', 'meaning': '材料', 'example_en': 'What are the ingredients in this salad?', 'example_ja': 'このサラダの材料はなんですか。', 'notes': '「〜の材料」と言うとき、後ろに続く前置詞はin, of, forが可能'},
    {'no': 515, 'word': 'capable', 'pos': '形容詞', 'meaning': '能力がある', 'example_en': 'Lucy Hill is quite capable of learning new skills.', 'example_ja': 'ルーシー・ヒルは新しいスキルを習得する能力がある。', 'notes': 'be capable of 〜の形で使われる。名: capability「能力」'},
    {'no': 516, 'word': 'conclusion', 'pos': '名詞', 'meaning': '結論', 'example_en': "We haven't reached a conclusion yet.", 'example_ja': '私達はまだ結論に達していない。', 'notes': 'reach a conclusion「結論に達する」、動: conclude「結論を出す、終える」、形: conclusive「決定的な、最終的な」、conclusive evidence「決定的な証拠」'},
    {'no': 517, 'word': 'emergency', 'pos': '名詞', 'meaning': '緊急事態', 'example_en': 'The emergency exit is down the hallway.', 'example_ja': '非常口は廊下の先です。', 'notes': 'emergency room (略: ER)「（病院の）緊急治療室」、the state of emergency「非常事態」'},
    {'no': 518, 'word': 'load', 'pos': '動詞', 'meaning': '積み込む', 'example_en': "They're loading the truck with boxes.", 'example_ja': '彼らはトラックに箱を積み込んでいる。', 'notes': '反: unload「荷物を降ろす」、名: load「荷物、積載量、仕事量」、形: loaded「荷物を積んだ」'},
    {'no': 519, 'word': 'punctual', 'pos': '形容詞', 'meaning': '時間を守る', 'example_en': 'Please try to be punctual.', 'example_ja': '時間を守るようにしてください。', 'notes': '名: punctuality「時間を守ること」、副: punctually「時間通りに」'},
    {'no': 520, 'word': 'possibility', 'pos': '名詞', 'meaning': '可能性', 'example_en': 'The two banks are discussing the possibility of a merger.', 'example_ja': 'その2つの銀行は合併の可能性について話し合っている。', 'notes': '「可能性がある事柄」という意味もある。形: possible「可能な」、副: possibly「もしかしたら、多分」(=maybe, perhaps)（probablyより可能性が低い）'},
    {'no': 521, 'word': 'journal', 'pos': '名詞', 'meaning': '専門誌', 'example_en': 'Mr. Johnson contributes to this trade journal.', 'example_ja': 'ジョンソンさんはこの業界誌に寄稿している。', 'notes': '専門性の高い雑誌・新聞を指す語。「日記」という意味もある。関: magazine「雑誌」、newspaper「新聞」、periodical「定期刊行物」'},
    {'no': 522, 'word': 'policy', 'pos': '名詞', 'meaning': '規則', 'example_en': 'We have a strict non-smoking policy.', 'example_ja': '当社には厳格な禁煙の規則があります。', 'notes': '「方針、政策、（保険の）契約」などの意味もある。insurance policy「保険契約」'},
    {'no': 523, 'word': 'appliance', 'pos': '名詞', 'meaning': '電化器具', 'example_en': 'The store carries a wide range of domestic appliances.', 'example_ja': 'その店は多様な家電製品を取り扱っている。', 'notes': 'appliance store「電器店」'},
    {'no': 524, 'word': 'approach', 'pos': '動詞', 'meaning': '話を持ちかける', 'example_en': 'Several companies have approached us.', 'example_ja': '数社が私達に話を持ちかけてきた。', 'notes': '「近づく、取り組む」などの意味もある。名: approach「手法、申し入れ、近づくこと」、形: approachable「親しみやすい」'},
    {'no': 525, 'word': 'standard', 'pos': '名詞', 'meaning': '基準', 'example_en': 'We have high safety standards.', 'example_ja': '当社は高い安全基準を持っています。', 'notes': '「規範」という意味もある。通常、standardsとsをつける。形: standard「標準の、基準となる」'},
    {'no': 526, 'word': 'valid', 'pos': '形容詞', 'meaning': '有効な', 'example_en': "You need a valid driver's license.", 'example_ja': 'あなたは有効な運転免許証が必要です。', 'notes': '「正当な」という意味もある。反: invalid「無効な」、動: validate「証明する」'},
    {'no': 527, 'word': 'eager', 'pos': '形容詞', 'meaning': '強く望んでいる', 'example_en': 'Our chef is eager to meet your catering needs.', 'example_ja': '私たちのシェフはあなたの食事のご要望を満たすことを強く望んでいます。', 'notes': '「熱心な」という意味もある。副: eagerly「熱心に」'},
    {'no': 528, 'word': 'opinion', 'pos': '名詞', 'meaning': '意見', 'example_en': 'We would like to know your opinions about our service.', 'example_ja': '私たちは当社のサービスに対するあなたのご意見をお聞きしたいと存じます。', 'notes': '同: view「意見、見方」、in my opinion「私の考えでは」'},
    {'no': 529, 'word': 'belongings', 'pos': '名詞', 'meaning': '持ち物', 'example_en': 'She packed her personal belongings in a bag.', 'example_ja': '彼女は私物をかばんに詰めた。', 'notes': 'この意味では常に複数形'},
    {'no': 530, 'word': 'assignment', 'pos': '名詞', 'meaning': '与えられた仕事', 'example_en': 'Marta has to complete the assignment by the end of October.', 'example_ja': 'マータはその仕事を10月末までに仕上げなければならない。', 'notes': '「（学生に与えられた）課題」という意味もある。動: assign「割り当てる」'},
    {'no': 531, 'word': 'innovative', 'pos': '形容詞', 'meaning': '革新的な', 'example_en': 'We develop innovative products and services.', 'example_ja': '当社は革新的な製品とサービスを開発しています。', 'notes': '動: innovate「（新しい技術・考えなどを）取り入れる」、名: innovation「革新、新しく取り入れたもの」、名: innovator「革新者」'},
    {'no': 532, 'word': 'supervise', 'pos': '動詞', 'meaning': '監督する', 'example_en': 'Dr. Hall supervises the research team.', 'example_ja': 'ホール博士が研究チームを監督する。', 'notes': '同: oversee「監督する」、名: supervision「監督」、名: supervisor「監督者」、形: supervisory「監督の」'},
    {'no': 533, 'word': 'credit', 'pos': '動詞', 'meaning': '(功績があると)認める', 'example_en': 'He is credited with developing popular video games.', 'example_ja': '彼は人気のビデオゲームを開発した功績を認められている。', 'notes': '同: attribute「〜のおかげだと考える」、名: credit「クレジット、功績、履修単位」'},
    {'no': 534, 'word': 'various', 'pos': '形容詞', 'meaning': 'さまざまな', 'example_en': 'We offer various training programs.', 'example_ja': '当社はさまざまな研修プログラムをご提供しております。', 'notes': '動: vary「変化する」、名: variety「種類、多様さ」、名: variation「変化、差」'},
    {'no': 535, 'word': 'analysis', 'pos': '名詞', 'meaning': '分析', 'example_en': "I'm doing a cost analysis of the project.", 'example_ja': '私はそのプロジェクトの費用分析をしている。', 'notes': '複数形はanalyses。動: analyze「分析する」、名: analyst「評論家、専門家」、形: analytical「分析的な」'},
    {'no': 536, 'word': 'reject', 'pos': '動詞', 'meaning': '却下する', 'example_en': 'The board of directors rejected my proposal.', 'example_ja': '取締役会は私の提案を却下した。', 'notes': '「拒否する、不合格にする、受け付けない」などの意味もある。同: turn down, refuse「却下する」、名: rejection「拒絶」'},
    {'no': 537, 'word': 'on behalf of', 'pos': '熟語', 'meaning': '〜を代表して', 'example_en': 'Mr. Robinson made a speech on behalf of the association.', 'example_ja': 'ロビンソンさんは協会を代表してスピーチをした。', 'notes': '「〜の代わりに」という意味もある'},
    {'no': 538, 'word': 'overlook', 'pos': '動詞', 'meaning': '見逃す', 'example_en': 'I overlooked errors in the report.', 'example_ja': '私は報告書の間違いを見逃した。', 'notes': '「大目にみる、（建物から）見える」などの意味もある'},
    {'no': 539, 'word': 'seal', 'pos': '動詞', 'meaning': '封をする', 'example_en': 'I sealed the box with tape.', 'example_ja': '私はテープで箱に封をした。', 'notes': '「密閉する、（建物・エリアなどを）封鎖する」などの意味もある。名: seal「封印、印鑑」'},
    {'no': 540, 'word': 'typical', 'pos': '形容詞', 'meaning': '典型的な', 'example_en': 'These temperatures are not typical for this time of year.', 'example_ja': 'これらの気温はこの時期としては普通ではありません。', 'notes': 'typical of 〜「典型的な〜」、副: typically「典型的に、通常は」'},
    {'no': 541, 'word': 'code', 'pos': '名詞', 'meaning': '規則', 'example_en': 'The company has a strict dress code.', 'example_ja': 'その会社は厳しい服装規則がある。', 'notes': '「法律、記号、番号」などの意味もある。area code「市外局番」、a code of conduct「行動規範」'},
    {'no': 542, 'word': 'connect', 'pos': '動詞', 'meaning': '接続する', 'example_en': 'You should connect the printer to the computer.', 'example_ja': 'プリンターをコンピュータに接続しなくてはなりません。', 'notes': '「電話をつなぐ」という意味もある。名: connection「接続、関係、乗り継ぎ」'},
    {'no': 543, 'word': 'general', 'pos': '形容詞', 'meaning': '大まかな', 'example_en': 'This map will give you a general overview of the area.', 'example_ja': 'この地図はその地区の大まかな概観を示します。', 'notes': '「一般的な、全体的な、普通の」などの意味もある。副: generally「一般的に」'},
    {'no': 544, 'word': 'nicely', 'pos': '副詞', 'meaning': 'うまく', 'example_en': 'He might say yes if you ask him nicely.', 'example_ja': 'もし彼にうまく頼めば、彼は受け入れてくれるかもしれない。', 'notes': '形: nice「よい」'},
    {'no': 545, 'word': 'orientation', 'pos': '名詞', 'meaning': 'オリエンテーション', 'example_en': 'We will hold an orientation for new employees next week.', 'example_ja': '当社では来週、新入社員のオリエンテーションを行います。', 'notes': '「信条、方針」などの意味もある。動: orient「向かわせる、位置を見定める」'},
    {'no': 546, 'word': 'positive', 'pos': '形容詞', 'meaning': '好意的な', 'example_en': 'We received positive reviews for our new fax machine.', 'example_ja': '当社は新しいファックス機に対して好意的な批評を得た。', 'notes': '「積極的な、肯定的な、陽性の」などの意味もある。反: negative「否定的な、悲観的な、陰性の」、副: positively「肯定的に、確実に」'},
    {'no': 547, 'word': 'however', 'pos': '副詞', 'meaning': 'どれだけ〜であろうと', 'example_en': 'We must handle customer complaints properly, however minor they may be.', 'example_ja': 'お客様からの苦情はたとえ小さなものであっても適切に対応しなければならない。', 'notes': '「しかし」(=but, nevertheless)という意味もある。同: no matter how「たとえ〜でも」'},
    {'no': 548, 'word': 'whether', 'pos': '接続詞', 'meaning': '〜かどうか', 'example_en': "I'll ask him whether he can finish it before lunch.", 'example_ja': '昼休み前に終わるかどうか彼に聞いてみます。', 'notes': '「〜であろうとなかろうと」という意味もある'},
    {'no': 549, 'word': 'calculate', 'pos': '動詞', 'meaning': '計算する', 'example_en': 'We calculated the cost of construction.', 'example_ja': '私たちは建設費用を計算した。', 'notes': '名: calculation「計算」、名: calculator「計算器」、形: calculated「計算された」'},
    {'no': 550, 'word': 'lean against', 'pos': '熟語', 'meaning': 'もたれかかる', 'example_en': 'The bicycle is leaning against the fence.', 'example_ja': '自転車がフェンスに立てかけられている。', 'notes': 'lean overは「身を乗り出す」、同: be leaning against = be propped up against「〜に立てかけられている」'},
    {'no': 551, 'word': 'enable', 'pos': '動詞', 'meaning': '可能にする', 'example_en': 'The new funds will enable us to continue our research.', 'example_ja': '新しい資金は私たちが調査を続けることを可能にします。', 'notes': 'enable 〈人〉 to 〈不定詞〉の形で使う。形: able to 〜「〜できる」、名: ability「能力」、en-は動詞を作る接頭辞'},
    {'no': 552, 'word': 'despite', 'pos': '前置詞', 'meaning': '〜にもかかわらず', 'example_en': "Mike didn't meet the sales target despite his efforts.", 'example_ja': 'マイクは努力したにもかかわらずセールス目標を達成できなかった。', 'notes': '同: in spite of 〜「〜にもかかわらず」'},
    {'no': 553, 'word': 'media', 'pos': '名詞', 'meaning': 'メディア', 'example_en': 'The event was reported in the media.', 'example_ja': 'その行事はメディアで報道された。', 'notes': 'television, radio, newspaper, magazine, Internetを含む。関: press「報道機関（主に印刷媒体）」'},
    {'no': 554, 'word': 'tax', 'pos': '名詞', 'meaning': '税金', 'example_en': 'You can get your taxes back.', 'example_ja': 'あなたは税金の払い戻しが受けられる。', 'notes': '動: tax「課税する、負担をかける」、名: taxation「課税」'},
    {'no': 555, 'word': 'trouble', 'pos': '名詞', 'meaning': '困難', 'example_en': 'I had trouble finding a good place to eat.', 'example_ja': '私は食事をするよい場所を探すのに苦労した。', 'notes': '同: problem「困難」、動: trouble「面倒をかける、困らせる、わざわざ〜する」、形: troublesome「面倒な、厄介な」'},
    {'no': 556, 'word': 'wish', 'pos': '動詞', 'meaning': 'したい', 'example_en': 'I wish to speak with the manager.', 'example_ja': 'マネージャーと話がしたいです。', 'notes': 'wish to 〜「〜したい」。「望む、願う」という意味もある。名: wish「望み、願い」、wishful thinking「希望的観測、甘い考え」'},
    {'no': 557, 'word': 'draw up', 'pos': '句動詞', 'meaning': '作成する', 'example_en': "He's drawing up a plan.", 'example_ja': '彼は計画を作成している。', 'notes': '同: make「作る」、write「書く」'},
    {'no': 558, 'word': 'formally', 'pos': '副詞', 'meaning': 'フォーマルに', 'example_en': 'We dressed formally for the ceremony.', 'example_ja': '私たちはそのセレモニーのためにフォーマルな服装をした。', 'notes': '形: formal「フォーマルな、格式ばった」、反: casually「カジュアルな、くつろいだ」'},
    {'no': 559, 'word': 'empty', 'pos': '形容詞', 'meaning': '空いている', 'example_en': 'The filing cabinets are almost empty.', 'example_ja': '書類整理用キャビネットはほとんど空いています。', 'notes': '動: empty「空にする」'},
    {'no': 560, 'word': 'core', 'pos': '形容詞', 'meaning': '主要な', 'example_en': 'Our core business is fresh fruit and vegetables.', 'example_ja': '当社の主要事業は新鮮な果物と野菜です。', 'notes': '同: main「主要な」、名: core「（りんごなどの）芯、中心」、core curriculum「中核教科課程」'},
    {'no': 561, 'word': 'crew', 'pos': '名詞', 'meaning': '(共同で作業をする)チーム', 'example_en': 'Our repair crew will be there in half an hour.', 'example_ja': '当社の修理スタッフが30分後にはお伺いします。', 'notes': '集団を指す語。「（船や飛行機の）乗組員・乗務員」という意味でも使われる'},
    {'no': 562, 'word': 'middle', 'pos': '名詞', 'meaning': '中旬', 'example_en': 'A friend of mine will visit me in the middle of September.', 'example_ja': '私の友人が9月中旬に私のところに来ます。', 'notes': '「真ん中、中間」というのが元の意味。mid-という接頭辞をつけて同じ意味を表すことができる。例: mid-September「9月中旬」、形: middle「中間の」'},
    {'no': 563, 'word': 'on foot', 'pos': '熟語', 'meaning': '徒歩で', 'example_en': 'It takes about fifteen minutes on foot.', 'example_ja': '徒歩で約15分です。', 'notes': '関: by car「車で」、by bus「バスで」、by train「電車で」'},
    {'no': 564, 'word': 'overseas', 'pos': '副詞', 'meaning': '海外で', 'example_en': 'Eddy worked overseas before joining this company.', 'example_ja': 'エディーはこの会社に入る前、外国で働いていた。', 'notes': '同: abroad「外国で」、形: overseas「海外の」'},
    {'no': 565, 'word': 'co-worker', 'pos': '名詞', 'meaning': '同僚', 'example_en': 'One of my co-workers is leaving the company.', 'example_ja': '私の同僚の一人が会社を辞める。', 'notes': 'co-は「一緒に」という意味を表す接頭辞(co-worker=「一緒に働いている人」)、同: colleague「同僚」'},
    {'no': 566, 'word': 'graduate', 'pos': '動詞', 'meaning': '卒業する', 'example_en': 'I recently graduated from university.', 'example_ja': '私は最近、大学を卒業した。', 'notes': '名: graduate「卒業生」、形: graduate「学士号を受けた」、名: graduation「卒業」、同: commencement〈加米〉「卒業式」'},
    {'no': 567, 'word': 'private', 'pos': '形容詞', 'meaning': '内密の', 'example_en': 'I had a private conversation with my supervisor.', 'example_ja': '私は上司と密談をした。', 'notes': '「私有の、民間の、個人の、内輪だけの」などの意味もある。in private「内密に」、副: privately「内密に、個人として」、名: privacy「プライバシー」'},
    {'no': 568, 'word': 'tip', 'pos': '名詞', 'meaning': 'ヒント', 'example_en': 'Here are some tips on how to stay healthy.', 'example_ja': '健康でいるためのヒントを以下に挙げます。', 'notes': '通常、tipsとsを付けて使われる。「先端、（レストラン等で渡す）チップ」などの意味もある。動: tip「チップを渡す」'},
    {'no': 569, 'word': 'agriculture', 'pos': '名詞', 'meaning': '農業', 'example_en': 'About fifty percent of the land is used for agriculture.', 'example_ja': '土地の約50パーセントは農業に使われている。', 'notes': '形: agricultural「農業の」、関: horticulture「園芸」'},
    {'no': 570, 'word': 'railing', 'pos': '名詞', 'meaning': '手すり', 'example_en': "He's holding onto the railing.", 'example_ja': '彼は手すりにつかまっている。', 'notes': '「柵、フェンス」を指すこともある。パート1で頻出'},
    {'no': 571, 'word': 'theme', 'pos': '名詞', 'meaning': 'テーマ', 'example_en': 'What is the theme of the conference?', 'example_ja': 'その会議のテーマは何ですか。', 'notes': '同: topic, subject「主題」'},
    {'no': 572, 'word': 'tie', 'pos': '名詞', 'meaning': 'つながり', 'example_en': 'We have strong ties with local businesses.', 'example_ja': '私たちは地元の企業と強いつながりがある。', 'notes': '「ネクタイ、引き分け」という意味もある。同: link「つながり」、動: tie「結ぶ」'},
    {'no': 573, 'word': 'fond', 'pos': '形容詞', 'meaning': '好ましい', 'example_en': 'I have fond memories of San Francisco.', 'example_ja': '私はサンフランシスコのよい思い出がある。', 'notes': 'be fond of 〜「〜が好き」'},
    {'no': 574, 'word': 'be supposed to', 'pos': '熟語', 'meaning': '〜することになっている', 'example_en': 'Mr. Brown was supposed to arrive an hour ago.', 'example_ja': 'ブラウンさんは1時間前に来ることになっていた。', 'notes': 'suppose は「思う、考える」という意味の動詞'},
    {'no': 575, 'word': 'related', 'pos': '形容詞', 'meaning': '関連のある', 'example_en': 'Applicants must have a degree in business or a related field.', 'example_ja': '応募者は経営学または関連分野での学位を持っていなければなりません。', 'notes': 'related to 〜「〜に関係がある」、動: relate「関係がある」、同: relating to 〜「〜に関連のある」、名: relation「関係」、名: relationship「関係」'},
    {'no': 576, 'word': 'confident', 'pos': '形容詞', 'meaning': '確信している', 'example_en': "I'm confident sales will pick up soon.", 'example_ja': '私は売り上げがもうすぐ回復することを確信しています。', 'notes': '「自信がある」という意味もある。名: confidence「自信、信頼、秘密」、形: confidential「秘密の、内密の」'},
    {'no': 577, 'word': 'I wonder if you', 'pos': '熟語', 'meaning': '〜していただけませんか', 'example_en': 'I wonder if you can help me.', 'example_ja': '手伝ってもらえませんか。', 'notes': "人に頼みごとをするときの表現。I was wondering if, I'm wondering if も同じ。wonderは「不思議に思う、知りたい」という意味"},
    {'no': 578, 'word': 'worth', 'pos': '前置詞', 'meaning': '〜の価値がある', 'example_en': 'The museum is worth a visit.', 'example_ja': 'その博物館には行く価値がある。', 'notes': 'worth 〜ing「〜する価値がある」、名: worth「価値」、形: worthless「価値のない」、形: worthy「尊敬すべき」'},
    {'no': 579, 'word': 'enroll', 'pos': '動詞', 'meaning': '申し込む', 'example_en': "I'd like to enroll in the drawing class.", 'example_ja': 'デッサンのクラスに申し込みたいと思います。', 'notes': '綴り: enrol〈英〉。後ろに続く前置詞はin〈加米〉、on/in〈英〉。同: sign up for 〜, apply for 〜「〜に申し込む」、同: register for 〜「〜に登録する」、名: enrollment「登録、入会」'},
    {'no': 580, 'word': 'environment', 'pos': '名詞', 'meaning': '環境', 'example_en': "We're trying to improve our work environment.", 'example_ja': '私たちは職場環境を向上させるように努めています。', 'notes': '「自然環境」という意味もある。形: environmental「環境に関する」、名: environmentalist「環境保護論者」'},
    {'no': 581, 'word': 'exactly', 'pos': '副詞', 'meaning': 'まったく', 'example_en': 'He told me exactly the same thing.', 'example_ja': '彼は私にまったく同じことを言いました。', 'notes': '「正確に、ちょうどに」という意味もある。同: precisely「まったく」、形: exact「正確な」'},
    {'no': 582, 'word': 'ideal', 'pos': '形容詞', 'meaning': '理想的な', 'example_en': 'The island is an ideal place for a family vacation.', 'example_ja': 'その島は家族旅行に理想的な場所です。', 'notes': '同: perfect「完璧な」、名: ideal「理想」、副: ideally「理想的に」'},
    {'no': 583, 'word': 'precisely', 'pos': '副詞', 'meaning': 'ちょうどに', 'example_en': "I arrived here at precisely six o'clock.", 'example_ja': '私はここに6時ちょうどに着いた。', 'notes': '「正確に、まったく」という意味もある。同: exactly, sharp「ちょうどに」、形: precise「正確な」、名: precision「正確さ」'},
    {'no': 584, 'word': 'suddenly', 'pos': '副詞', 'meaning': '突然に', 'example_en': 'The finance minister suddenly resigned.', 'example_ja': '財務大臣は突然、辞任した。', 'notes': '形: sudden「突然の」'},
    {'no': 585, 'word': 'capacity', 'pos': '名詞', 'meaning': '定員', 'example_en': 'The hall was filled to capacity.', 'example_ja': 'ホールは定員いっぱいだった。', 'notes': '「能力、任務、最大生産量」などの意味もある。filled to capacity「定員いっぱい、満席」という意味'},
    {'no': 586, 'word': 'admission', 'pos': '名詞', 'meaning': '入場料', 'example_en': 'Admission is free for members.', 'example_ja': '会員は入場無料です。', 'notes': '「入ること、入場許可、入学許可、告白」という意味もある。動: admit「認める、入場を許可する」、関: admission fee「入場料」'},
    {'no': 587, 'word': 'advantage', 'pos': '名詞', 'meaning': '利点', 'example_en': 'What are the advantages of this system?', 'example_ja': 'このシステムの利点は何ですか。', 'notes': '「有利な点、優位性、長所」などの意味もある。take advantage of 〜「〜を利用する」、反: disadvantage「不利な点、短所」、形: advantageous「有利な」'},
    {'no': 588, 'word': 'anniversary', 'pos': '名詞', 'meaning': '記念日', 'example_en': 'Tomorrow is our wedding anniversary.', 'example_ja': '明日は私たちの結婚記念日です。', 'notes': 'the twentieth anniversary「20周年記念」'},
    {'no': 589, 'word': 'candidate', 'pos': '名詞', 'meaning': '候補者', 'example_en': 'There are five candidates for the position.', 'example_ja': 'その職には5人の候補者がいます。', 'notes': '職の話をしているときはapplicant「応募者」とほぼ同じ意味になる'},
    {'no': 590, 'word': 'career', 'pos': '名詞', 'meaning': '職業', 'example_en': 'I was interested in a career in journalism.', 'example_ja': '私は報道関係の職業に興味があった。', 'notes': '「職歴」という意味もある'},
    {'no': 591, 'word': 'imagine', 'pos': '動詞', 'meaning': '想像する', 'example_en': 'The garden was more beautiful than I had imagined.', 'example_ja': 'その庭園は私が想像していたより美しかった。', 'notes': '名: imagination「想像、想像力」、形: imaginative「想像力のある」'},
    {'no': 592, 'word': 'perfect', 'pos': '形容詞', 'meaning': '最適な', 'example_en': 'Kate is the perfect candidate for the job.', 'example_ja': 'ケイトはその仕事に最適な候補者です。', 'notes': '「完璧な、最高の」などの意味もある。同: ideal「理想的な」、副: perfectly「完璧に」、動: perfect「完全にする」、名: perfection「完璧」'},
    {'no': 593, 'word': 'potential', 'pos': '形容詞', 'meaning': '潜在的な', 'example_en': 'How can we reach our potential customers more effectively?', 'example_ja': '私たちはどうやったらもっと効果的に潜在的な顧客に知ってもらうことができるでしょうか。', 'notes': '「可能性がある」という意味もある。形容詞として使われるときは、常に名詞の前に来る。名: potential「可能性」、副: potentially「潜在的に」'},
    {'no': 594, 'word': 'separate', 'pos': '形容詞', 'meaning': '別の', 'example_en': "We'll send your order in two separate shipments.", 'example_ja': 'ご注文の品はふたつの別の便でお送りします。', 'notes': '「関係のない」という意味もある。同: different「別の」、動: separate「分ける」、副: separately「別々に」'},
    {'no': 595, 'word': 'apart from', 'pos': '前置詞', 'meaning': '〜以外に', 'example_en': 'Apart from baseball, what sports do you like?', 'example_ja': '野球以外にスポーツは何が好きですか。', 'notes': '「〜に加えて」(=besides, in addition to)という意味もある。同: except for 〜「〜以外に」'},
    {'no': 596, 'word': 'mechanical', 'pos': '形容詞', 'meaning': '機械的な', 'example_en': 'The flight was canceled due to mechanical failure.', 'example_ja': '機械的な故障により、その便は運行が中止された。', 'notes': '名: machine(可算名詞)「機械」、名: machinery(不可算名詞)「機械」、副: mechanically「機械的に」'},
    {'no': 597, 'word': 'rest', 'pos': '名詞', 'meaning': '残り', 'example_en': "There's not much work for the rest of the day.", 'example_ja': '今日、これから残りの時間はあまり仕事がない。', 'notes': '「休息、休止」という意味もある。同: remainder「残り」、動: rest「休む、もたれかかる」'},
    {'no': 598, 'word': 'unique', 'pos': '形容詞', 'meaning': '珍しい', 'example_en': 'The gift shop carries unique jewelry made of seashells.', 'example_ja': 'そのギフトショップでは貝殻でできた珍しいジュエリーを販売している。', 'notes': '「独特の、唯一の」などの意味もある'},
    {'no': 599, 'word': 'disappointed', 'pos': '形容詞', 'meaning': 'がっかりした', 'example_en': 'We are disappointed with the results.', 'example_ja': '私たちはその結果にがっかりした。', 'notes': '動: disappoint「がっかりさせる」、形: disappointing「がっかりさせるような」、名: disappointment「失望」'},
    {'no': 600, 'word': 'modest', 'pos': '形容詞', 'meaning': '多くない', 'example_en': "I've saved a modest amount of money.", 'example_ja': '私は少額のお金を貯めた。', 'notes': '「謙虚な、控えめな」などの意味もある。名: modesty「謙遜」'},
]

CHOICE_LABELS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

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
