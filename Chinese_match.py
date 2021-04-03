import re
const_ad='E:\\maogai\\maogai'
for i in range(1,131):
        with open(const_ad+str(i)+'.txt','r',encoding='utf-8') as lines:
            for line in lines:
                regex_str = ".*?([\u4E00-\u9FA5]+).*?"
                match_obj = re.findall(regex_str, line)
                excep1="得 0 分，满分 1 分"
                excep2="问题 "
                
                not_match12=not (re.findall(excep1,line) or re.findall(excep2,line))

                excep3="正确答案"                
                not_match3=re.findall(excep3,line) 
                #print("{} {} {}",match_obj,not_match12,not_match3)

                excep4="快速链接"
                excep5="我的机构"
                excep6="课程3的标签2"
                excep7="教学创新大赛评审"
                excep8=" 毛泽东思想和中国特色社会主义理论体系概论 课程间导航 复习总测试 执行测验: 复习总测试"
                excep9="隐藏课程菜单"
                excep10="课程"
                excep11="复习总测试"
                excep12="我的小组"
                excep13="小组主页"
                excep14="执行测验"
                excep15="测试信息"
                excep16="计时的测验"
                elseth=re.findall(excep4,line)  or re.findall(excep5,line) or re.findall(excep6,line) or re.findall(excep7,line) or re.findall(excep8,line) or re.findall(excep9,line) or re.findall(excep10,line)  or re.findall(excep11,line) or re.findall(excep12,line) or re.findall(excep13,line) or re.findall(excep14,line) or re.findall(excep15,line) or re.findall(excep16,line)
                
                need1="【第八"
                n1=re.findall(need1,line)
                need0="【第"
                n0=re.findall(need0,line)
                if(n0):
                    if(n1):
                        head=True
                    else:
                        head=False
                if(match_obj and not_match12 and not not_match3 and not elseth ):
                    with open('E://total.txt','a') as f:
                        if(n1):
                             f.write(line)
                        else:
                             if( head ):
                                 f.write(line)


                        
#找出第一章节

        