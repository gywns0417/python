
class Numbering: #성적 입력과 출력 클래스
    def num_input(self,msg):
     while True:
         try:
             
           global number
           number=int(input(msg))
           
           if len(str(number))==10:
               return number
               break
               

           else:
               print("학번은 10자리 입니다.")
         except:
             print("숫자만 입력해 주세요.")

    def ab_input(self,msg):
     while True:
         try:
          
           abs=int(input(msg))
           
           if abs > 20:
              print("최대 결석 시수는 20일 입니다.")
              
           else:
               return abs
               break

         except:
           print("정수인 숫자만 입력해 주세요.")

    def as_input(self,msg):
      while True:
         try:
           ass=int(input(msg))
          
           if ass > 20 or ass<0:
              print("과제 점수는 0~20점 입니다.")
           else:
               return ass
               break

         except:
             print("정수인 숫자만 입력해 주세요.")

    def mid_input(self,msg):
      while True:
         try:
           mid=int(input(msg))
           
           if mid > 30 or mid<0:
              print("중간고사 점수는 0~30점 입니다.")
           else:
              return mid
              break

         except:
             print("정수인 숫자만 입력해 주세요.")

    def last_input(self,msg):
      while True:
         try:
           last=int(input(msg))
           
           if last > 30 or last <0:
              print("기말고사 점수는 0~30점 입니다.")
           else:
               return last
               break

         except:
             print("정수인 숫자만 입력해 주세요.")


class TxtCount: #txt파일 입출력 함수 및 파일 생성 함수
    def maketxt(self,txt):
        
     
          try:
            global f
            f = open(txt, 'r')
            ncount=len(f.readlines()) #임시저장.txt 파일을 읽어와 한명(6줄)을 이용해 20명 초과 불가로 만든다.
            if ncount > 120:
              print("최대 수강생인 20명을 초과하였습니다. 더 이상 입력하실 수 없습니다. 파일을 수정하여 주십시오.")
           

              

            else:
               pass
               
              
                  
          except: #파일이 존재하지 않는 오류가 발생하면 파일을 생성시킨다.
            print("파일이 존재하지 않아 파일을 생성합니다. 입력된 점수들은 이곳에 기록됩니다.")
            f = open(txt, 'w')
            
           

    def close(self):
         f.close()

    def read(self,txt):
         open(txt, 'r')
    
    def write(self,txt):
               f = open(txt,'w')
               f.write("학번 : " + str(n) + "\n")
               f.write("결석 :" + str(abscore) + "\n")
               f.write("과제 점수 : " + str(asscore) + "\n")
               f.write("중간고사 점수 :" + str(midscore) + "\n")
               f.write("기말고사 점수 :" + str(lastscore) + "\n")
               f.write("총점 :" + str(allscore) + "\n")
               f.write("----------------------\n")
              


class Choice:
    import re
    global re

    def cc(self): #총점을 학점.txt파일에 저장
    
    
     i="5"
     choicenumber = "임시저장.txt"
     with open(choicenumber) as file_object:
          contents = file_object.read()
      
     sohard = re.findall("\d+", contents)
  
     sumscore = sohard[5] #총점만 골라 학점.txt 파일에 저장
     try:
         
           f = open("학점.txt" ,'a')
           f.write(sumscore + "\n")
           f.close()
               
     except:
         pass
 

    def calculator(self): #학점.txt 파일에서 총점을 불러와 학점으로 변환
         
         
         global hakjum
         global cal
         
         hakjum = None

         cel = "학점.txt"
         with open(cel) as file_object:
             contents = file_object.read()
         cal = re.findall("\d+", contents)
         return cal

         calsort = cal.sorted(reverse = True) #여기서부터 실패. 학점을 내림차순으로 정렬한 calsort 가 오류는 없지만 결과값을 가져오지 않음.
         


         calA = round(int(0.3*len(calsort))) #학점 갯수 * 0.3 하여 반올림
         calB = round(int(0.7*len(calsort)))
         calC = round(int(1.0*len(calsort)))

         if (calA/len(calsort))*100 <=30: #반올림한 값을 학점 갯수로 나눈 후 100을 곱함
             hakjum = "A"
           
         elif (calB/len(calsort))*100 <=70:
             hakjum = "B"

         elif (calA/len(calsort))*100 <=100:
             hakjum = "C"

         if 20-ababscore < "5":
             hakjum = "F"

        
class Last(TxtCount):  #정보를 다 취합해 kyungnam.txt 파일 완성

         
      def write(self,txt):
               f = open(txt,'w')
               f.write("학번 : " + str(n) + "\n")
               f.write("결석 :" + str(abscore) + "\n")
               f.write("과제 점수 : " + str(asscore) + "\n")
               f.write("중간고사 점수 :" + str(midscore) + "\n")
               f.write("기말고사 점수 :" + str(lastscore) + "\n")
               f.write("총점 :" + str(allscore) + "\n")
               f.write("학점 : " + str(hakjum) + "\n")
               f.write("----------------------\n")


c1=Numbering()
c2=TxtCount()
c3=Choice()
c4=Last()
print("안녕하세요. 경남대학교 성적관리 프로그램에 오신 것을 환영합니다.\n")


n=c1.num_input("성적을 입력할 학생의 학번을 입력해주세요. :")

print("입력하신 학번은 " + str(number) + " 입니다.")

abscore=c1.ab_input("결석 시수를 입력해 주세요 : ")
asscore=c1.as_input("과제 점수를 입력해 주세요 : ")
midscore=c1.mid_input("중간고사 점수를 입력해 주세요 : ")
lastscore=c1.last_input("기말고사 점수를 입력해 주세요 : ")
allscore= 20-abscore + asscore + midscore + lastscore

import time
print("잠시만 기다려 주세요...")
time.sleep(2)

c2.maketxt("임시저장.txt")
c2.write("임시저장.txt")
c3.cc()
c3.calculator()

print("학번 : " + str(n) )
print("출석 점수 :" + str(abscore))
print("과제 점수 : " + str(asscore))
print("중간고사 점수 :" + str(midscore))
print("기말고사 점수 :" + str(lastscore))
print("총점 : " + str(allscore))
if len(cal) >= 10: #유의미한 학점 계산을 위해 10명 이상의 성적을 입력했을때만 학점 출력하게 함.
        print("학점: " + str(hakjum))

else:
        print("성적을 입력한 학생이 10명 미만이라 학점 계산이 불가합니다.")

c4.write("kyungnam.txt")


 
     
