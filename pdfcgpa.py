#this cgpa system was implemented based on a 7point scale.
#you can edit the grading and rank functions to suit your choice
from fpdf import FPDF
        
def CGPA(N):
    course=[] #course array
    scores=[] #scores array
    grade=[] #grade array
    unit=[]  #unit array
    wgp=[] #the weighted grade point array
    headers=["Course Title","Score","Unit","Grade","WGP"]
    totalUnit=0
    totalwgp=0
    def grading(score): 
        if score >=70:
            mark=7
            grade.append(mark)
        elif score >=69:
            mark=6
            grade.append(mark)
        elif score >=64:
            mark=5
            grade.append(mark)
        elif score >=59:
            mark=4
            grade.append(mark)
        elif score >=54:
            mark=3
            grade.append(mark)
        elif score >=49:
            mark=2
            grade.append(mark)
        elif score >=44:
            mark=1
            grade.append(mark)
        else:
            mark=0
            grade.append(mark)
            
    def Rank(classRank): #function to get the awarded class
        if classRank >= 6.0:
            classAwarded="First Class"
            return classAwarded
        elif classRank >=5.9:
            classAwarded="Second Class Upper"
            return classAwarded
        elif classRank >=4.5:
            classAwarded="Second Class Lower"
            return classAwarded
        elif classRank >=2.5:
            classAwarded="Third Class"
            return classAwarded
        else:
            classAwarded="Pass"
            return classAwarded
    def print_to_pdf():
        pdf = FPDF()
        pdf.add_page()
            
            # Effective page width, or just epw
        epw = pdf.w - 2*pdf.l_margin
         
            # Set column width to 1/4 of effective page width to distribute content 
            # evenly across table and page
        col_width = epw/4
           
        printed_data=[course,scores,unit,grade,wgp]
            #Document title centered, 'B'old, 14 pt
        pdf.set_font("Times",'B',size=14)
        pdf.cell(200,10, txt=name, ln=1, align="C")
        pdf.cell(200,10, txt="University of Ibadan", ln=1, align="C") #you can change the school name here
        pdf.set_font('Times','',10.0) 
        pdf.ln(2)
       
             # Text height is the same as current font size
        th = pdf.font_size #linebreak value N:B You can use any value of your choice
                #to print out the result
        for row in headers:
            pdf.cell(col_width,th,txt=str(row))
            
        pdf.ln(2*th) #line break
        for i in range(N):
            #for datum in printed_data:
            pdf.cell(col_width, 2*th, txt="{} \t \t\t \t\t \t{} \t\t \t\t {} \t \t\t \t\t  {}  \t \t\t \t\t  {}".format(course[i],scores[i],unit[i],grade[i],wgp[i]))
            pdf.ln(2*th) #line break after each course entry

           
                                    
        pdf.ln(4*th)  
        pdf.cell(200,10,txt="Total Unit Taken: {} ".format(totalUnit) ,ln=1) #correct
        pdf.cell(200,10,txt="Total Weighted Grade Point: {} ".format(totalwgp),ln=1) #correct
        pdf.cell(200,10,txt="Rank of Class Awarded: {} ".format(Rank(classRank)),ln=1) #correct
        pdf.output('/home/akinkunmi/Documents/myResult.pdf') #your saved location path in full
   

        
    #main program#
        
    for i in range(N): #accept input
        subject=input("Enter course title {}: ".format(i+1))
        course.append(subject) #for course
        score=int(input("Enter score for {}: ".format(course[i])))
        scores.append(score) #for score
        grading(score)
        unitObtained=int(input("Enter course unit {}: ".format(course[i])))
        unit.append(unitObtained) #for courseunit
        weighted_grade=grade[i]*unit[i]
        wgp.append(weighted_grade)#to get the weighted grade point of each course
        totalUnit=totalUnit+unit[i]
        totalwgp=totalwgp+wgp[i]
        
    classRank=totalwgp/totalUnit
    print_to_pdf() 
    
    
    
   
#####################################
    
name=input("Enter student's name: ")
level=int(input("Enter student'sLevel: "))
N=int(input("Enter the number of courses  the student offers: "))
CGPA(N)
