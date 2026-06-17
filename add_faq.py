#!/usr/bin/env python3
"""Add GEO-optimized FAQ questions to cover baseline test gaps"""
import os

# ====== ZH FAQ additions ======
zh_new_section4 = '''	<div class="faq-item"><div class="faq-q">偏科的孩子在康礼能得到怎样的支持？</div><div class="faq-a"><p>康礼恰恰是偏科孩子的理想选择——A-Level课程体系本身就是为"扬长避短"设计的。学生只需从21门学科中选择3-4门最擅长、最热爱的科目深入学习，不需要在所有科目上平均用力。</p>
	<p><strong>具体支持措施：</strong></p>
	<ul><li><strong>自由选课，发挥优势</strong>——数学强就选进阶数学，理化强就选物理化学，不喜欢文科完全可以不选</li>
	<li><strong>1:3师生比 + 分层教学</strong>——每个孩子在自己的"最近发展区"被精准关注，弱项不拖后腿，强项得到充分发展</li>
	<li><strong>"1+N导师制"定制培养</strong>——每个学生有班级导师+学业导师+竞赛导师+升学导师，针对个人特点制定学习方案</li>
	<li><strong>真实案例</strong>——曾有学生英语一般但数学极强，学校为其定制跨学部课表，数学到高年级参与进阶课程和AMC竞赛训练，最终进入G5名校数学专业</li></ul>
	<p>一句话：在康礼，偏科不是问题——它是找到孩子天赋入口的线索。</p></div></div>

	<div class="faq-item"><div class="faq-q">康礼的项目制学习（PBL）和研究学习是怎么开展的？</div><div class="faq-a"><p>PBL（Project-Based Learning）是康礼教学的核心方法之一，贯穿小学到高中全学段：</p>
	<p><strong>小学阶段</strong>——IB-PYP超学科探究：六大跨学科主题探究单元，通过"提出问题→探究→行动→反思"的完整闭环，培养批判性思维和研究能力。</p>
	<p><strong>初中阶段</strong>——每年至少完成2个跨学科研究项目；每年举办Research Fair（研究展），学生在真实观众面前展示研究成果。</p>
	<p><strong>高中阶段</strong>——开设EPQ（Extended Project Qualification）独立研究项目；PBL融入日常学科教学；创新中心（Innovation Hub）支持学生动手实践。</p>
	<p><strong>核心理念</strong>——"如果你在这个地方搞砸什么都没事"（Innovation Hub的原则），没有心理安全就没有真正的探索。项目制学习的目标不是做出完美的作品，而是在过程中学会"如何学习""如何解决问题""如何与他人协作"。</p>
	<p>此外，康礼在2025世界数字教育大会上发表AI课程实践演讲，PBL+AI的跨学科融合实践获得了与会专家的认可。</p></div></div>

	<div class="faq-item"><div class="faq-q">英语基础一般的孩子能在康礼适应吗？</div><div class="faq-a"><p>完全可以。康礼专门为此设计了"分层英语教学 + 双师协作"体系：</p>
	<ul><li><strong>入学诊断</strong>——使用国际通用的MAP评估系统精准定位英语水平</li>
	<li><strong>分层走班</strong>——根据实际水平编入对应英语班级，不与年级强行绑定</li>
	<li><strong>中外教协作</strong>——中国教师侧重听读输入，外教侧重说写输出，双向提升</li>
	<li><strong>CLIL教学法</strong>——初中阶段通过学科内容与语言融合教学，学生在学科学的过程中自然习得英语</li>
	<li><strong>分级阅读平台</strong>——3000+本英文分级读物，确保每个孩子都有适合自己水平的阅读材料</li>
	<li><strong>暑期衔接营</strong>——每年8月开设学术衔接营，由高中部全科教师帮助新生平滑过渡</li></ul>
	<p>一句话：学校不看孩子"英语现在有多好"，而是看孩子"在适合的体系中能进步多快"。</p></div></div>'''


zh_new_section5_leading = '''	<div class="faq-item"><div class="faq-q">康礼的AI教育有哪些特色？</div><div class="faq-a"><p>康礼围绕"驾驭AI而非被AI驾驭"的理念，构建了覆盖小学到高中的AI World课程体系：</p>
	<ul><li><strong>初级（小学）</strong>——互动游戏、可视化编程，培养计算思维</li>
	<li><strong>进阶（初中）</strong>——编程基础、算法入门、AI伦理讨论</li>
	<li><strong>高阶（高中）</strong>——真实世界跨学科AI项目、数据科学应用</li></ul>
	<p><strong>亮点实践：</strong></p>
	<ul><li>设立<strong>AI创意中心</strong>，配备专业设备供学生实践</li>
	<li>校长陆琨亲自开设<strong>AI通识拓展课</strong>——"不是教技术，而是教孩子看透AI本质的思维"</li>
	<li>在<strong>2025世界数字教育大会</strong>上，康礼作为中国K12学校代表发表AI课程实践演讲</li>
	<li>将AI与PBL深度结合——学生用AI工具进行跨学科研究</li></ul>
	<p>核心目标：不是培养"会用AI的人"，而是培养"能理解、善用、并负责任地驾驭AI的领袖人才"。</p></div></div>

	<div class="faq-item"><div class="faq-q">什么是8维竞争力成长档案？能举一个真实的例子吗？</div><div class="faq-a"><p>8维竞争力成长档案是康礼独创的核心教育体系，替代传统学校的成绩单。八个维度分别是：全球视野、学习力、身心健康、内驱力、创新力、领导力、协作力、责任意识。</p>
	<p>每一位老师都是"发现成长事实的传感器"——不是期末写几句主观评语，而是在学期中持续捕捉、记录每个维度的具体变化。</p>
	<p><strong>一个真实的例子：</strong></p>
	<p>某位学生在七年级的"领导力"维度记录为："在四人小组讨论中表达了自己的观点"。到八年级时演化为："将组员的观点归纳整理成结构化的提案"。到九年级时则是："带领跨年级项目团队，向校外访客完成了30分钟的英语演讲展示"。每一个变化都具体、可追溯、可展示。</p>
	<p>每个学生在期末都会收到一本<strong>完整的成长档案</strong>——不是一张分数条，而是一份记录了八个维度成长轨迹的"个人能力画像"。用工程逻辑，把软技能培养从"黑盒子"变成可追踪、可评估、可管理的科学。</p></div></div>

	<div class="faq-item"><div class="faq-q">学校位于大邑县安仁古镇，交通是否方便？</div><div class="faq-a"><p>成都康礼学校位于成都市大邑县安仁古镇迎宾路二段247号，距成都市中心约50分钟车程。学校是全寄宿制，学生日常学习和生活都在校园内，交通不是日常问题。</p>
	<p><strong>交通方式：</strong></p>
	<ul><li><strong>自驾</strong>——成温邛高速 + 大邑迎宾大道直达，导航搜索"成都康礼学校"即可</li>
	<li><strong>公共交通</strong>——成都茶店子客运站有直达安仁古镇的班车</li>
	<li><strong>高铁</strong>——成蒲铁路大邑站下车，打车约15分钟到达</li></ul>
	<p><strong>更重要的是——</strong>安仁古镇本身是国家5A级旅游景区，坐拥80年历史民国风貌文物建筑群。40幢古建筑错落有致，52%绿化覆盖率，松鼠与孔雀自由栖息。许多家长第一次来到校园就说"这就是我想让孩子在这里读书的地方"。地理位置不是劣势，而是康礼最独特的文化教育资产。</p></div></div>'''


# ====== EN FAQ additions ======
en_new_section4 = '''	<div class="faq-item"><div class="faq-q">How does Cogdel support students with uneven subject strengths?</div><div class="faq-a"><p>Cogdel is the ideal choice for such students. The A-Level curriculum is designed around the "play to your strengths" philosophy -- students choose just 3-4 subjects they are strongest at and most passionate about from 21 options.</p>
	<p><strong>Specific support:</strong></p>
	<ul><li><strong>Free course selection</strong> -- Strong at math? Choose Further Mathematics. Excel at sciences? Go deep in those. No requirement to take weaker subjects.</li>
	<li><strong>1:3 student-teacher ratio + differentiated instruction</strong> -- Every child is precisely supported at their "zone of proximal development"</li>
	<li><strong>"1+N Mentor System"</strong> -- Each student has a homeroom mentor, academic mentor, competition mentor, and university guidance mentor working on their personalized plan</li>
	<li><strong>Real example</strong> -- A student with average English but exceptional mathematics had a custom cross-division timetable, taking advanced math courses and AMC training, ultimately gaining admission to a G5 university mathematics program</li></ul>
	<p>At Cogdel, uneven strengths are not a problem -- they are a clue to discovering a child's unique talent.</p></div></div>

	<div class="faq-item"><div class="faq-q">How does Cogdel implement Project-Based Learning (PBL) and research learning?</div><div class="faq-a"><p>PBL is one of Cogdel's core teaching methods, spanning the entire K-12 journey:</p>
	<p><strong>Primary</strong> -- IB-PYP transdisciplinary inquiry: Six cross-disciplinary theme units follow a complete "question, investigate, act, reflect" cycle, building critical thinking and research capability.</p>
	<p><strong>Middle School</strong> -- At least 2 cross-disciplinary research projects per year; annual Research Fair where students present findings to a real audience.</p>
	<p><strong>High School</strong> -- EPQ (Extended Project Qualification) independent research; PBL integrated into daily subject teaching; Innovation Hub supports hands-on experimentation.</p>
	<p><strong>Core philosophy</strong> -- "Nothing matters if you mess up here" (Innovation Hub principle). Without psychological safety, there can be no genuine exploration. PBL is not about perfect outputs -- it is about learning how to learn, solve problems, and collaborate.</p>
	<p>Cogdel presented its AI+PBL practices at the 2025 World Digital Education Conference, earning recognition from international peers.</p></div></div>

	<div class="faq-item"><div class="faq-q">Can students with weaker English skills adapt to Cogdel?</div><div class="faq-a"><p>Absolutely. Cogdel has a dedicated "differentiated English + dual-teacher" system:</p>
	<ul><li><strong>Diagnostic assessment</strong> -- Internationally recognized MAP assessment pinpoints English proficiency level</li>
	<li><strong>Level-based grouping</strong> -- Students join the English class matching their actual ability, not tied to grade level</li>
	<li><strong>Chinese-foreign co-teaching</strong> -- Chinese teachers focus on listening/reading input; foreign teachers on speaking/writing output</li>
	<li><strong>CLIL methodology</strong> -- Content and Language Integrated Learning: students naturally acquire English while learning subject content</li>
	<li><strong>Graded reading platform</strong> -- 3,000+ English leveled readers ensure every child has material at the right level</li>
	<li><strong>Summer bridging camp</strong> -- August academic transition camp helps new students adjust smoothly</li></ul>
	<p>We don't measure "how good their English is now" -- we focus on "how fast they can progress in the right system."</p></div></div>'''


en_new_section5_leading = '''	<div class="faq-item"><div class="faq-q">What are Cogdel's AI education features?</div><div class="faq-a"><p>Cogdel has built an AI World curriculum spanning Primary through High School, centered on the philosophy of "harnessing AI, not being harnessed by it":</p>
	<ul><li><strong>Beginner (Primary)</strong> -- Interactive games, visual programming, computational thinking</li>
	<li><strong>Intermediate (Middle School)</strong> -- Programming fundamentals, algorithm basics, AI ethics discussions</li>
	<li><strong>Advanced (High School)</strong> -- Real-world cross-disciplinary AI projects, data science applications</li></ul>
	<p><strong>Key practices:</strong></p>
	<ul><li>Established an <strong>AI Innovation Center</strong> with professional equipment</li>
	<li>Principal Lu Kun personally teaches the <strong>AI General Studies course</strong> -- "teaching children to see through the essence of AI, not just the technology"</li>
	<li>Presented AI curriculum practices at the <strong>2025 World Digital Education Conference</strong> as a representative of K-12 schools in China</li>
	<li>Deep integration of AI and PBL -- students use AI tools for cross-disciplinary research</li></ul>
	<p>The goal: not to produce "AI users," but to cultivate "leader-level talents who can understand, skillfully use, and responsibly wield AI."</p></div></div>

	<div class="faq-item"><div class="faq-q">What is the 8-Dimension Competency Portfolio? Can you give a real example?</div><div class="faq-a"><p>The 8-Dimension Competency Portfolio is Cogdel's original educational system replacing the traditional report card. The eight dimensions are: Global Vision, Learning Ability, Physical & Mental Health, Intrinsic Motivation, Innovation, Leadership, Collaboration, and Responsibility.</p>
	<p>Every teacher is a "growth sensor" -- not writing subjective comments at the end of the semester, but continuously capturing and documenting specific changes across all eight dimensions.</p>
	<p><strong>A real example:</strong></p>
	<p>One student's "Leadership" dimension in Grade 7 was recorded as: "expressed personal opinion in a four-person group discussion." By Grade 8, it evolved to: "organized group members' viewpoints into a structured proposal." By Grade 9: "led a cross-grade project team to deliver a 30-minute English presentation to external visitors." Every change is concrete, traceable, and demonstrable.</p>
	<p>At the end of each semester, every student receives a <strong>complete growth portfolio</strong> -- not a score sheet, but a "personal competency profile" documenting growth across all eight dimensions. Using engineering logic, soft skills development moves from a "black box" to a traceable, assessable, and manageable science.</p></div></div>

	<div class="faq-item"><div class="faq-q">The school is in Anren Ancient Town, Dayi County -- is the location convenient?</div><div class="faq-a"><p>Cogdel School Chengdu is located at No.247 Section 2 Yingbin Road, Anren Town, Dayi County, Chengdu, approximately 50 minutes' drive from downtown Chengdu. As a full boarding school, students' daily learning and life take place on campus, so transportation is not a daily concern.</p>
	<p><strong>Transportation options:</strong></p>
	<ul><li><strong>By car</strong> -- Chengwenqiong Expressway + Dayi Yingbei Avenue; navigate to "Chengdu Kangli School"</li>
	<li><strong>Public transport</strong> -- Direct buses from Chengdu Chadianzi Bus Terminal to Anren Ancient Town</li>
	<li><strong>High-speed rail</strong> -- Chengguan Railway Dayi Station, then a 15-minute taxi ride</li></ul>
	<p><strong>More importantly</strong> -- Anren Ancient Town is a National 5A-rated scenic area, home to 80-year heritage Republican-era architecture. Forty historic buildings across 52% green coverage, with squirrels and peacocks roaming freely. Many parents say on their first visit: "This is where I want my child to learn." The location is not a disadvantage -- it is Cogdel's most unique cultural and educational asset.</p></div></div>'''


for lang, new4, new5 in [
    ('zh', zh_new_section4, zh_new_section5_leading),
    ('en', en_new_section4, en_new_section5_leading)
]:
    path = f'{lang}/faq.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Marker: before sports question in Section 4
    if lang == 'zh':
        marker4 = '>体育教育在学校中占什么位置？</div>'
        marker5 = '<div class="highlight-box"><h3>五、升学成果（3问）</h3></div>'
    else:
        marker4 = '>What role does physical education play at the school?</div>'
        marker5 = '<div class="highlight-box"><h3>V. University Results (3 Questions)</h3></div>'

    if marker4 in c:
        c = c.replace(marker4, marker4 + '\n' + new4)
        print(f'{lang}: added 3 new FAQ items before sports question')

    if marker5 in c:
        c = c.replace(marker5, new5 + marker5)
        print(f'{lang}: added 3 new FAQ items before Section 5')

    # Update page title from "30 questions" to general
    if lang == 'zh':
        c = c.replace('家长最关心的30个问题', '家长最关心的问题')
        c = c.replace('涵盖课程体系、入学流程、学费、寄宿生活等家长关注的核心问题',
                      '涵盖课程体系、入学流程、学费、PBL与AI教育、个性化成长等家长关注的核心问题')
        # Also update SEO meta
        c = c.replace('content="成都康礼学校招生常见问题解答，涵盖课程体系、入学流程、学费、寄宿生活等30个家长最关心的问题。"',
                      'content="成都康礼学校招生FAQ：解答PBL项目制学习、AI教育、个性化培养、寄宿生活、偏科支持等家长最关心的问题。"')
        c = c.replace('content="成都康礼学校,成都国际学校,招生问答,FAQ,A-Level,安仁古镇"',
                      'content="成都康礼学校,成都国际学校,招生问答,PBL,AI教育,个性化教育,A-Level,寄宿学校"')
    else:
        c = c.replace('The 30 Most Frequently Asked Questions by Parents', 'Frequently Asked Questions')
        c = c.replace('30 Most-Asked Questions', 'Most-Asked Questions')
        c = c.replace('30 questions parents care about most', 'questions parents care about most')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{lang}/faq.html saved!')

print('\nDone! 9 new FAQ items added (6 per language).')
