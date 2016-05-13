# DAY_14
2016년 05월 12일  
crawling / TDD / python 개발 환경 구축

## 학습 내용
* fibonacci 과제 리뷰
  * n이 들어가서 가장 먼저 해야할 것은 cache에 n이 들어 있는지부터 확인

* crawling
  * 크롤링에서 중요한 것은 어떻게 찾느냐이다. => 휴리스틱!
  * 각 홈페이지에 정책이 있다. naver.com/robots.txt
  * (크롬)개발자 도구 > element에서 찾기 > 네트워크도 확인해보고...
  * 네이버 블로그 긁기 연습 => requests, BeautifulSoup
  * 직방 긁기 연습 => requests, json ( api 찾아서 )

* Test
  * 테스트 주도 개발 => RED / GREEN / refactor
  * Continuous Intergration => 지속적 통합의 구축

* python 개발 환경 구축
  * pyenv -> virtualenv -> autoenv

* 기업특강
  * 특강 기업: Fastcampus
  * 이직과 교육에 초점을 두고 대학과는 차별화 되지만(학문적 vs 실전적) 동등한 수준의 경쟁력을 보장하는 것을 추구
  * 코스매니저라는 특이한 role 이 있고 이는 mini CEO가 되어 하나의 과정을 총괄


* 숙제
  * 클래스 구현 => FastcampusSchool, FastcampusPerson
  * 네이버 블로그 크롤링 1~100 페이지
