#!/usr/bin/env python3
"""Translate EN apply.html from Chinese to English"""
path = r'en\apply.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# Navigation
c = c.replace('lang="zh-CN"', 'lang="en"')
c = c.replace('预约访校 - ', 'Book a Visit - ')
c = c.replace('预约参观成都康礼学校，实地感受5A景区里的未来学校。',
              'Book a campus visit at Cogdel School Chengdu.')
c = c.replace('成都康礼学校,预约访校,招生咨询,校园参观',
              'Cogdel School,book a visit,campus tour,admissions')
c = c.replace('class="active">中文', 'href="../zh/apply.html">中文')
c = c.replace('English</a>', 'class="active">English</a>')
c = c.replace('../en/index.html', '../en/apply.html')
c = c.replace('English</div>', '')
c = c.replace('nav"><a href="apply.html"', 'nav"><a href="apply.html"')

# Navigation menu items
c = c.replace('学校介绍', 'About')
c = c.replace('关于康礼', 'About Cogdel')
c = c.replace('环境设施', 'Campus')
c = c.replace('管理团队', 'Leadership')
c = c.replace('师资团队', 'Faculty')
c = c.replace('课程体系', 'Curriculum')
c = c.replace('课程总览', 'Overview')
c = c.replace('小学部', 'Primary')
c = c.replace('初中部', 'Middle School')
c = c.replace('高中部', 'High School')
c = c.replace('学生成长', 'Student Life')
c = c.replace('升学成果', 'Results')
c = c.replace('新闻速递', 'News')
c = c.replace('校长说', "Principal's Column")
c = c.replace('择校指南', 'School Selection')
c = c.replace('课程与教学', 'Teaching')
c = c.replace('招生问答', 'FAQ')

# Another pass for nested ones
c = c.replace('Overview</a>', 'Overview</a>')
c = c.replace('Primary</a>', 'Primary</a>')

# Page content
c = c.replace('实地感受5A景区里的未来学校', 'Experience the Future School in a 5A Scenic Area')
c = c.replace('首页', 'Home')
c = c.replace('预约访校表单', 'Book a Campus Visit')
c = c.replace('请填写以下信息，提交后将直接推送至招生系统，招生老师将在24小时内与您联系：',
              'Please fill in the form below. Your information will be sent to our admissions system directly. Our team will contact you within 24 hours.')
c = c.replace('招生流程', 'Admissions Process')
c = c.replace('第1步：咨询预约', 'Step 1: Consultation')
c = c.replace('第2步：校园访校', 'Step 2: Campus Visit')
c = c.replace('第3步：入学评估', 'Step 3: Assessment')
c = c.replace('第4步：录取沟通', 'Step 4: Admissions Discussion')
c = c.replace('第5步：注册入学', 'Step 5: Enrolment')
c = c.replace('与招生老师沟通学生年级、学习背景、兴趣方向及家庭关注点',
              'Discuss with our admissions team')
c = c.replace('实地体验校园环境、课程特色、学生支持体系与寄宿生活',
              'Experience our campus, curriculum, and boarding life')
c = c.replace('根据申请年级进行学术测试、英语测试、面谈或作品集（艺术方向）等综合评估',
              'Academic testing, English assessment, and interview')
c = c.replace('学校根据评估结果提供课程路径建议、升学方向建议与录取沟通',
              'Curriculum pathway and university guidance')
c = c.replace('完成录取确认、学籍/入学材料提交与开学前衔接准备',
              'Complete enrolment and pre-term preparation')

# Form fields
c = c.replace('学生姓名 *', 'Student Name *')
c = c.replace('请输入学生姓名', 'Student name')
c = c.replace('当前年级 *', 'Current Grade *')
c = c.replace('请选择年级', 'Select grade')
c = c.replace('小学1年级', 'Grade 1')
c = c.replace('小学2年级', 'Grade 2')
c = c.replace('小学3年级', 'Grade 3')
c = c.replace('小学4年级', 'Grade 4')
c = c.replace('小学5年级', 'Grade 5')
c = c.replace('初中6年级', 'Grade 6')
c = c.replace('初中7年级', 'Grade 7')
c = c.replace('初中8年级', 'Grade 8')
c = c.replace('高中9年级', 'Grade 9')
c = c.replace('高中10年级', 'Grade 10')
c = c.replace('高中11年级', 'Grade 11')
c = c.replace('高中12年级', 'Grade 12')
c = c.replace('家长手机号 *', 'Parent Phone *')
c = c.replace('请输入手机号', 'Phone number')
c = c.replace('家长微信（选填）', 'WeChat (optional)')
c = c.replace('请输入微信号', 'WeChat ID')
c = c.replace('其他问题（选填）', 'Questions (optional)')
c = c.replace('请输入您想了解的问题', 'Any questions?')

# Button
c = c.replace('提交预约', 'Submit')
c = c.replace('提交中...', 'Submitting...')
c = c.replace('提交成功！', 'Submitted Successfully!')
c = c.replace('您的预约信息已推送至招生系统，招生老师将在24小时内与您联系。',
              'Your information has been sent to our admissions system. Our team will contact you within 24 hours.')

# Principal quote - fixed regex
old_q = '"学校定期举办全学段开放日、夏令营和主题营地活动，欢迎家长和学生实地感受康礼的教育氛围。"'
new_q = '"We regularly hold open days, summer camps, and themed activities. We warmly invite parents and students to experience the Cogdel educational atmosphere in person."'
c = c.replace(old_q, new_q)

# Footer
c = c.replace('成都康礼学校', 'Cogdel School Chengdu')
c = c.replace('成都市大邑县安仁古镇迎宾路二段247号',
              'No.247 Section 2 Yingbin Road, Anren Town, Dayi County, Chengdu')
c = c.replace('招生热线：400-803-6661', 'Admissions: +86 400-803-6661')
c = c.replace('快速链接', 'Quick Links')
c = c.replace('关注我们', 'Follow Us')
c = c.replace('微信公众号：成都市大邑康礼外国语学校', 'WeChat: Cogdel School Chengdu')
c = c.replace('视频号/小红书/抖音：成都市大邑康礼外国语学校', 'Video/Xiaohongshu/Douyin: Cogdel School')
c = c.replace('校长账号：陆琨校长', 'Principal: Lu Kun')

# Breadcrumb
c = c.replace('预约访校', 'Book a Visit')

# H1
c = c.replace('<h1>预约访校</h1>', '<h1>Book a Campus Visit</h1>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print('EN apply.html translated!')
