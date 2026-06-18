#!/usr/bin/env python3
"""SEO optimize ALL remaining pages"""
import os, re

seo = {
    'zh/faq.html': {
        't': '招生问答 - 成都康礼学校 | PBL·AI教育·个性化培养·寄宿·偏科支持',
        'd': '成都康礼学校招生FAQ：解答PBL项目制学习、AI教育、8维成长档案、个性化培养、寄宿生活、偏科支持、A-Level选课、英语分层教学等家长最关心的36个问题。',
        'k': '成都康礼学校,招生问答,PBL,AI教育,个性化教育,A-Level,寄宿学校,偏科,英语分层,国际学校FAQ'
    },
    'zh/highschool.html': {
        't': '高中部 - 成都康礼学校 | IGCSE+A-Level 21门+AP | 1+N导师制 | 艺术名校',
        'd': '成都康礼学校高中部：IGCSE+A-Level 21门学科+AP，文理艺自由组合，1+N导师制定制培养，雅思名师校内备考，艺术方向100%QS TOP10。AI World课程+EPQ独立研究。',
        'k': '成都康礼学校,高中部,IGCSE,A-Level 21门,AP,1+N导师制,艺术升学,EPQ,AI课程,雅思'
    },
    'zh/primary.html': {
        't': '小学部 - 成都康礼学校 | IB-PYP+国家课程 | 英语分层·一生一群',
        'd': '成都康礼学校小学部：IB-PYP+国家义务教育课程双轨并行，语文数学对标成都顶级公办，英语跨年级分层教学，五年级KET最高级。一生一群定制反馈。',
        'k': '成都康礼学校,小学部,IB-PYP,双语,英语分层,KET,国家课程,国际小学,个性化'
    },
    'zh/middle.html': {
        't': '初中部 - 成都康礼学校 | 中西融合+CLIL英语 | 6年级启动升学规划',
        'd': '成都康礼学校初中部：国家课程+国际化校本课程（融合UK Key Stage3），CLIL英语教学，理科实验占比40%，6年级启动升学规划，100%学生参与AMC/BPhO等国际竞赛。',
        'k': '成都康礼学校,初中部,中西融合,CLIL,升学规划,AMC,BPhO,竞赛,PET,国际初中'
    },
    'zh/team.html': {
        't': '管理团队 - 成都康礼学校 | 陆琨校长(清华)·中外教育者·15+年经验',
        'd': '成都康礼学校管理团队：陆琨校长（清华大学+中欧MBA，前飞机工程师+投资人），中外副校长15年以上国际教育经验，1+N导师制管理架构。',
        'k': '成都康礼学校,管理团队,陆琨,清华校长,国际学校管理,外方校长'
    },
    'zh/faculty.html': {
        't': '师资团队 - 成都康礼学校 | 40%G5藤校·60%硕博·100%海外·1:3师生比',
        'd': '成都康礼学校师资：40%毕业于英国G5和美国藤校，60%硕士或博士学历，100%海外学习工作经验，100%持A-Level/AP认证。师生比1:3，1+N导师制。',
        'k': '成都康礼学校,师资,G5藤校,硕博,海外经历,A-Level认证,师生比,外教'
    },
    'zh/news.html': {
        't': '新闻速递 - 成都康礼学校 | 招生手册·京领百强榜·夏令营·IB培训',
        'd': '成都康礼学校最新新闻：2026-2027招生手册、入选京领品牌价值百强榜、小学英文夏令营、IB-PYP官方培训、心理课堂、国际教育峰会等校园动态。',
        'k': '成都康礼学校,新闻,招生手册,京领百强榜,夏令营,IB培训,校园动态'
    },
    'zh/principal.html': {
        't': '校长说 - 成都康礼学校 | 陆琨：择校指南·课程教学·学生成长',
        'd': '陆琨校长专栏：择校指南（怎么选国际学校）、课程与教学（A-Level/IB/AP怎么选）、学生成长（PBL/AI/个性化/寄宿/手机管理）等深度教育思考。',
        'k': '成都康礼学校,校长说,陆琨,择校指南,国际学校选择,教育理念,课程教学'
    },
    'zh/principal-guide.html': {
        't': '择校指南 - 校长说 | 成都康礼学校 | 国际学校怎么选·转轨指南',
        'd': '陆琨校长择校指南：五个硬指标判断国际学校、转轨三大问题、值不值的匹配账、择校不看排名看什么。成都国际学校选择必读。',
        'k': '成都康礼学校,择校指南,国际学校怎么选,转轨,陆琨,五个指标,择校'
    },
    'zh/principal-teaching.html': {
        't': '课程与教学 - 校长说 | 成都康礼学校 | AI时代能力·英语工具论',
        'd': '陆琨校长谈课程与教学：AI时代不可替代的能力、英语不是学科是思考工具、PBL作为基础设施而非特色课、投资人课堂、8维成长档案。',
        'k': '成都康礼学校,课程与教学,AI教育,英语学习,PBL,8维档案,陆琨,投资人课堂'
    },
    'zh/principal-growth.html': {
        't': '学生成长 - 校长说 | 成都康礼学校 | 手机管理·体育自信·寄宿生活',
        'd': '陆琨校长谈学生成长：手机管理的自律与自由、体育是自信第一来源、寄宿不是离开家是走进更大的家、学生会不是干部俱乐部。',
        'k': '成都康礼学校,学生成长,手机管理,体育教育,寄宿生活,陆琨,自律,自信'
    },
    'zh/results-admissions.html': {
        't': '升学录取 - 成都康礼学校 | 牛剑·G5·艺术TOP10·竞赛喜报',
        'd': '成都康礼学校升学录取喜报：牛津剑桥、英国G5精英大学、世界TOP100、艺术QS TOP10、国际竞赛金奖。记录每位学子的精彩时刻。',
        'k': '成都康礼学校,升学录取,牛津剑桥,G5,艺术TOP10,竞赛喜报,A-Level'
    },
    'zh/apply.html': {
        't': '预约访校 - 成都康礼学校 | 参观5A景区校园·招生咨询·全年滚动招生',
        'd': '预约参观成都康礼学校，实地感受5A级安仁古镇里的未来学校。全年滚动招生，电话400-803-6661。招生流程+kehu51表单在线提交。',
        'k': '成都康礼学校,预约访校,参观校园,招生咨询,开放日,安仁古镇'
    },
    # EN versions
    'en/faq.html': {
        't': 'FAQ - Cogdel School Chengdu | PBL·AI·Boarding·Personalized Learning',
        'd': 'Cogdel School FAQ: 36 questions on PBL, AI World curriculum, 8-Dimension portfolio, personalized education, boarding life, A-Level selection, and English support.',
        'k': 'Cogdel School,FAQ,PBL,AI education,boarding,personalized learning,A-Level,international school'
    },
    'en/highschool.html': {
        't': 'High School - Cogdel School | IGCSE+A-Level 21 Subjects+AP | 1+N Mentor',
        'd': 'Cogdel High School: IGCSE+A-Level (21 subjects)+AP, free course selection, 1+N Mentor System, on-campus IELTS, EPQ research, AI World curriculum, 100% art QS TOP10.',
        'k': 'Cogdel School,high school,IGCSE,A-Level,AP,mentor,EPQ,AI curriculum,IELTS'
    },
    'en/primary.html': {
        't': 'Primary - Cogdel School | IB-PYP+Bilingual | Differentiated English | KET',
        'd': 'Cogdel Primary: IB-PYP+National Curriculum dual-track, Chinese/Math benchmarked to top Chengdu standards, cross-grade English co-teaching, KET by Grade 5.',
        'k': 'Cogdel School,primary,IB-PYP,bilingual,English,KET,international primary'
    },
    'en/middle.html': {
        't': 'Middle School - Cogdel School | China-West Fusion+CLIL | 100% Competitions',
        'd': 'Cogdel Middle School: National curriculum+UK KS3 integration, CLIL English, 40% lab ratio, Grade 6 career planning, 100% AMC/BPhO competition participation.',
        'k': 'Cogdel School,middle school,CLIL,UK Key Stage 3,AMC,BPhO,competitions'
    },
    'en/team.html': {
        't': 'Leadership - Cogdel School | Principal Lu Kun (Tsinghua)·15+yr Experience',
        'd': 'Cogdel leadership: Principal Lu Kun (Tsinghua University+CEIBS MBA, ex-aircraft engineer+investor). Chinese and international VPs with 15+ years education experience.',
        'k': 'Cogdel School,leadership,Lu Kun,Tsinghua,international school management'
    },
    'en/faculty.html': {
        't': 'Faculty - Cogdel School | 40% G5/Ivy·60% Master/PhD·100% Overseas·1:3 Ratio',
        'd': 'Cogdel faculty: 40% UK G5/US Ivy League, 60% Master/PhD, 100% overseas experience, 100% A-Level/AP certified. 1:3 student-teacher ratio, 1+N mentor system.',
        'k': 'Cogdel School,faculty,G5,Ivy League,Master,PhD,A-Level certified,mentor'
    },
    'en/news.html': {
        't': 'News - Cogdel School | Admissions·KingLead Top 100·Summer Camp·IB Training',
        'd': 'Latest Cogdel news: 2026-2027 Admissions Brochure, KingLead Brand Value Top 100, English Summer Camp, IB-PYP training, psychology program, education summit.',
        'k': 'Cogdel School,news,admissions,KingLead,summer camp,IB training,updates'
    },
    'en/principal.html': {
        't': "Principal's Column - Cogdel School | Lu Kun: Selection·Teaching·Growth",
        'd': "Principal Lu Kun's column: school selection guide, curriculum & teaching insights, student growth philosophy on PBL, AI, boarding, sports, and personalized learning.",
        'k': 'Cogdel School,principal,Lu Kun,school selection,education,PBL,AI,personalized'
    },
    'en/principal-guide.html': {
        't': "School Selection Guide - Cogdel School | How to Choose an International School",
        'd': "Principal Lu Kun's guide: 5 indicators for international schools, 3 questions before transferring, cost-benefit analysis. Essential Chengdu international school selection guide.",
        'k': 'Cogdel School,school selection,guide,international school,Lu Kun,transfer,indicators'
    },
    'en/principal-teaching.html': {
        't': "Teaching & Curriculum - Cogdel School | AI Skills·PBL·English as Tool",
        'd': "Principal Lu Kun on teaching: irreplaceable AI-era capabilities, English as thinking tool not exam subject, PBL as infrastructure, investor classroom, 8-Dimension portfolio.",
        'k': 'Cogdel School,teaching,curriculum,AI skills,PBL,English,8-Dimension,Lu Kun'
    },
    'en/principal-growth.html': {
        't': "Student Growth - Cogdel School | Phone Policy·Sports·Boarding·Self-Discipline",
        'd': "Principal Lu Kun on growth: phone management and self-discipline, sports as confidence source, boarding as bigger home, student council as service not management.",
        'k': 'Cogdel School,student growth,phone policy,sports,boarding,self-discipline,Lu Kun'
    },
    'en/results-admissions.html': {
        't': 'Admissions Results - Cogdel School | Oxbridge·G5·Art TOP10·Gold Medals',
        'd': 'Cogdel university admissions: Oxbridge offers, UK G5, World TOP100, QS Art TOP10 for 5 years, international competition gold medals. Every student achievement.',
        'k': 'Cogdel School,admissions,Oxbridge,G5,art TOP10,competition,results'
    },
    'en/apply.html': {
        't': 'Book a Visit - Cogdel School | Campus Tour·Admissions·5A Scenic Area',
        'd': 'Book a campus visit at Cogdel School in 5A Anren Ancient Town. Rolling admissions. Call +86 400-803-6661. Submit inquiry via online form.',
        'k': 'Cogdel School,book a visit,campus tour,admissions,Anren Ancient Town,open day'
    },
}

count = 0
for fp, u in seo.items():
    if not os.path.exists(fp):
        print(f'SKIP: {fp}')
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    o = c
    if 't' in u:
        c = re.sub(r'<title>[^<]*</title>', f'<title>{u["t"]}</title>', c)
    if 'd' in u:
        c = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{u["d"]}">', c)
    if 'k' in u:
        c = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{u["k"]}">', c)
    if c != o:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1
        print(f'OK: {fp}')
    else:
        print(f'NC: {fp}')

print(f'\nDone! Updated {count} files')
