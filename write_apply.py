#!/usr/bin/env python3
import os

zh = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>预约访校 - 成都康礼学校</title>
<meta name="description" content="预约参观成都康礼学校，实地感受5A景区里的未来学校。">
<link rel="stylesheet" href="../css/style.css?v=1781603834">
</head>
<body>
<div class="lang-bar"><a href="" class="active">中文</a><span>|</span><a href="../en/index.html">English</a></div>
<header class="header"><div class="header-inner">
<a href="index.html" class="logo"><img src="../images/bg1.png" alt="Cogdel" class="logo-img"></a>
<button class="menu-toggle" onclick="document.querySelector('.nav').classList.toggle('open')">&#9776;</button>
<ul class="nav">
<li><a href="about.html">学校介绍</a><div class="dropdown"><a href="about.html">关于康礼</a><a href="campus.html">环境设施</a><a href="team.html">管理团队</a><a href="faculty.html">师资团队</a></div></li>
<li><a href="curriculum.html">课程体系</a><div class="dropdown"><a href="curriculum.html">课程总览</a><a href="primary.html">小学部</a><a href="middle.html">初中部</a><a href="highschool.html">高中部</a></div></li>
<li><a href="student-life.html">学生成长</a></li>
<li><a href="results.html">升学成果</a></li>
<li><a href="news.html">新闻速递</a></li>
<li><a href="principal.html">校长说</a><div class="dropdown"><a href="principal-guide.html">择校指南</a><a href="principal-teaching.html">课程与教学</a><a href="principal-growth.html">学生成长</a></div></li>
<li><a href="faq.html">招生问答</a></li>
<li><a href="apply.html" class="nav-cta">预约访校</a></li>
<li><span class="nav-phone">&#9742; 400-803-6661</span></li>
</ul></div></header>
<section class="page-banner"><div><h1>预约访校</h1><div class="en">Book a Visit</div></div></section>
<div class="breadcrumb"><a href="index.html">首页</a> &#187; 预约访校</div>
<main class="article"><h1>预约访校</h1><div class="meta">实地感受5A景区里的未来学校</div><div class="content">

<div class="highlight-box"><h3>招生流程</h3>
<p><strong>第1步：咨询预约</strong> -- 与招生老师沟通学生年级、学习背景、兴趣方向及家庭关注点<br>
<strong>第2步：校园访校</strong> -- 实地体验校园环境、课程特色、学生支持体系与寄宿生活<br>
<strong>第3步：入学评估</strong> -- 根据申请年级进行学术测试、英语测试、面谈或作品集（艺术方向）等综合评估<br>
<strong>第4步：录取沟通</strong> -- 学校根据评估结果提供课程路径建议、升学方向建议与录取沟通<br>
<strong>第5步：注册入学</strong> -- 完成录取确认、学籍/入学材料提交与开学前衔接准备</p></div>

<h2>预约访校表单</h2><p>请填写以下信息，提交后将直接推送至招生系统，招生老师将在24小时内与您联系：</p>

<div style="background:var(--wh); border-radius:12px; box-shadow:0 4px 24px rgba(0,0,0,.08); padding:8px; margin:24px 0; min-height:550px;">
  <iframe src="https://f.kehu51.com/html/565955/20260313094149513.html" style="width:100%; height:550px; border:none;" scrolling="no"></iframe>
</div>

<div class="highlight-box"><h3>校长说</h3><p>"学校定期举办全学段开放日、夏令营和主题营地活动，欢迎家长和学生实地感受康礼的教育氛围。"</p></div>

</div></main>

<footer class="footer"><div class="footer-inner">
<div><h4>成都康礼学校</h4><p>成都市大邑县安仁古镇迎宾路二段247号<br>招生热线：400-803-6661</p></div>
<div><h4>快速链接</h4><p><a href="about.html">学校介绍</a><br><a href="curriculum.html">课程体系</a><br><a href="student-life.html">学生成长</a><br><a href="results.html">升学成果</a><br><a href="faq.html">招生问答</a><br><a href="apply.html">预约访校</a></p></div>
<div><h4>关注我们</h4><p>微信公众号：成都市大邑康礼外国语学校<br>视频号/小红书/抖音：成都市大邑康礼外国语学校<br>校长账号：陆琨校长</p></div>
</div><div class="footer-bottom">&copy; 2026 Cogdel School Chengdu. [2026-06-17 17:10 v3]</div></footer>
<script src="../js/main.js?v=1781603834"></script>
</body>
</html>'''

# Build EN from ZH with translations
replacements = [
    ('lang="zh-CN"', 'lang="en"'),
    ('预约访校 - 成都康礼学校', 'Book a Visit - Cogdel School Chengdu'),
    ('预约参观成都康礼学校，实地感受5A景区里的未来学校。', 'Book a campus visit at Cogdel School Chengdu.'),
    ('<a href="" class="active">中文', '<a href="../zh/apply.html">中文'),
    ('../en/index.html', '../en/apply.html'),
    ('English</a>', 'class="active">English</a>'),
    ('class="nav-cta">预约访校', 'class="nav-cta">Book a Visit'),
    ('预约访校</a></p>', 'Book a Visit</a></p>'),
    ('<h1>预约访校</h1>', '<h1>Book a Campus Visit</h1>'),
    ('预约访校表单', 'Book a Campus Visit'),
    ('请填写以下信息，提交后将直接推送至招生系统，招生老师将在24小时内与您联系：',
     'Fill in the form below. Your information goes directly to our admissions system. We will contact you within 24 hours.'),
    ('招生流程', 'Admissions Process'),
    ('第1步：咨询预约', 'Step 1: Consultation'),
    ('第2步：校园访校', 'Step 2: Campus Visit'),
    ('第3步：入学评估', 'Step 3: Assessment'),
    ('第4步：录取沟通', 'Step 4: Admissions Discussion'),
    ('第5步：注册入学', 'Step 5: Enrolment'),
    ('与招生老师沟通学生年级、学习背景、兴趣方向及家庭关注点',
     'Discuss learning background, interests, and priorities with our admissions team'),
    ('实地体验校园环境、课程特色、学生支持体系与寄宿生活',
     'Experience our campus, curriculum, student support, and boarding life'),
    ('根据申请年级进行学术测试、英语测试、面谈或作品集（艺术方向）等综合评估',
     'Academic testing, English assessment, interview, or portfolio review (art applicants)'),
    ('学校根据评估结果提供课程路径建议、升学方向建议与录取沟通',
     'Curriculum pathway recommendations, university guidance, and admissions discussion'),
    ('完成录取确认、学籍/入学材料提交与开学前衔接准备',
     'Complete enrolment confirmation and pre-term preparation'),
    ('校长说', 'From the Principal'),
    ('"学校定期举办全学段开放日、夏令营和主题营地活动，欢迎家长和学生实地感受康礼的教育氛围。"',
     '"We regularly hold open days, summer camps, and themed activities. We warmly invite parents and students to experience the Cogdel educational atmosphere in person."'),
    ('学校介绍', 'About'),
    ('关于康礼', 'About Cogdel'),
    ('环境设施', 'Campus'),
    ('管理团队', 'Leadership'),
    ('师资团队', 'Faculty'),
    ('课程体系', 'Curriculum'),
    ('课程总览', 'Overview'),
    ('小学部', 'Primary'),
    ('初中部', 'Middle School'),
    ('高中部', 'High School'),
    ('学生成长', 'Student Life'),
    ('升学成果', 'Results'),
    ('新闻速递', 'News'),
    ('校长说</a>', "Principal's Column</a>"),
    ('择校指南', 'School Selection'),
    ('课程与教学', 'Teaching'),
    ('招生问答', 'FAQ'),
    ('首页', 'Home'),
    ('实地感受5A景区里的未来学校', 'Experience the Future School in a 5A Scenic Area'),
    ('成都康礼学校', 'Cogdel School Chengdu'),
    ('成都市大邑县安仁古镇迎宾路二段247号',
     'No.247 Section 2 Yingbin Road, Anren Town, Dayi County, Chengdu'),
    ('招生热线：400-803-6661', 'Admissions: +86 400-803-6661'),
    ('快速链接', 'Quick Links'),
    ('关注我们', 'Follow Us'),
    ('微信公众号：成都市大邑康礼外国语学校', 'WeChat: Cogdel School Chengdu'),
    ('视频号/小红书/抖音：成都市大邑康礼外国语学校', 'Video/Xiaohongshu/Douyin: Cogdel School'),
    ('校长账号：陆琨校长', 'Principal: Lu Kun'),
]

en = zh
for old, new in replacements:
    en = en.replace(old, new)

en = en.replace('class="active">中文', 'href="../zh/apply.html">中文')

# Fix remaining nav links
en = en.replace("Principal's Column</a><div class=\"dropdown\"><a href=\"principal-guide.html\">School Selection",
                "Principal's Column</a><div class=\"dropdown\"><a href=\"principal-guide.html\">School Selection")
en = en.replace('<a href="principal-teaching.html">Teach', '<a href="principal-teaching.html">Teach')  # no-op check

path = '.'
with open(os.path.join(path, 'zh/apply.html'), 'w', encoding='utf-8') as f:
    f.write(zh)
print('zh/apply.html written')

with open(os.path.join(path, 'en/apply.html'), 'w', encoding='utf-8') as f:
    f.write(en)
print('en/apply.html written')

# Quick verify
print('ZH has kehu51:', 'kehu51' in zh)
print('EN has kehu51:', 'kehu51' in en)
print('ZH has form/iframe:', 'iframe' in zh)
print('EN has form/iframe:', 'iframe' in en)
