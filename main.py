from dapi import Dapi
import sys
# myAPIKey = sys.argv[1]
api = Dapi()


group20 = {'기업집단': ['삼성', '현대자동차', '에스케이', '엘지', '롯데', '포스코', '한화', '지에스', '현대중공업', '농협', '신세계',
                         '케이티', '씨제이', '한진', '두산', '엘에스', '부영', '대림', '미래에셋', '금호아시아나', '에쓰-오일', '현대백화점',
                         '카카오', '한국투자금융', '교보생명보험', '효성', '하림', '영풍', '대우조선해양', '케이티앤지', '에이치디씨', '케이씨씨',
                         '코오롱', '대우건설', '오씨아이', '이랜드', '태영', 'SM', 'DB', '세아', '네이버', '넥슨', '한국타이어', '호반건설',
                         '셀트리온', '중흥건설', '넷마블', '아모레퍼시픽', '태광', '동원', '한라', '삼천리', '에이치엠엠', '장금상선', 'IMM인베스트먼트',
                         '한국지엠', '동국제강', '다우키움', '금호석유화학', '애경', '하이트진로', '유진', 'KG', '삼양'],
            '대표회사': ['삼성전자', '현대자동차', 'SK', 'LG', '롯데지주', '포스코', '한화', 'GS', '한국조선해양', '농협경제지주', '신세계',
                         '케이티', 'CJ', '대한항공', '두산', 'LS', '부영', '대림산업', '미래에셋캐피탈', '금호산업', 'S-Oil', '현대백화점',
                         '카카오', '한국금융지주', '교보생명보험', '효성', '하림지주', '영풍', '대우조선해양', '케이티앤지', 'HDC', '케이씨씨',
                         '코오롱', '대우건설', 'OCI', '이랜드월드', '태영건설', '티케이케미칼', 'DB', '세아홀딩스', 'NAVER', '엔엑스씨',
                         '한국앤컴퍼니', '호반건설',
                         '셀트리온홀딩스', '중흥건설', '넷마블', '아모레퍼시픽그룹', '태광산업', '동원엔터프라이즈', '한라홀딩스', '삼천리', 'HMM', '장금상선',
                         '아이엠엠인베스트먼트',
                         '한국지엠', '동국제강', '키움증권', '금호석유화학', 'AK홀딩스', '하이트진로홀딩스', '유진기업', 'KG케미칼', '삼양홀딩스']}

group19 = {'기업집단': ['삼성', '현대자동차', '에스케이', '엘지', '롯데', '포스코', '한화', '지에스', '현대중공업', '농협', '신세계',
                         '케이티', '씨제이', '한진', '두산', '엘에스', '부영', '대림', '미래에셋', '금호아시아나', '에쓰-오일', '현대백화점',
                         '카카오', '한국투자금융', '교보생명보험', '효성', '하림', '영풍', '대우조선해양', '케이티앤지', '에이치디씨', '케이씨씨',
                         '코오롱', '대우건설', '오씨아이', '이랜드', '태영', 'SM', 'DB', '세아', '네이버', '넥슨', '한국타이어', '호반건설',
                         '셀트리온', '중흥건설', '넷마블', '아모레퍼시픽', '태광', '동원', '한라', '삼천리',
                         '한국지엠', '동국제강', '다우키움', '금호석유화학', '애경', '하이트진로', '유진'],
            '대표회사': ['삼성전자', '현대자동차', 'SK', 'LG', '롯데지주', '포스코', '한화', 'GS', '한국조선해양', '농협경제지주', '신세계',
                         '케이티', 'CJ', '대한항공', '두산', 'LS', '부영', '대림산업', '미래에셋캐피탈', '금호산업', 'S-Oil', '현대백화점',
                         '카카오', '한국금융지주', '교보생명보험', '효성', '하림지주', '영풍', '대우조선해양', '케이티앤지', 'HDC', '케이씨씨',
                         '코오롱', '대우건설', 'OCI', '이랜드월드', '태영건설', '티케이케미칼', 'DB', '세아홀딩스', 'NAVER', '엔엑스씨',
                         '한국앤컴퍼니', '호반건설',
                         '셀트리온홀딩스', '중흥건설', '넷마블', '아모레퍼시픽그룹', '태광산업', '동원엔터프라이즈', '한라홀딩스', '삼천리',
                         '한국지엠', '동국제강', '키움증권', '금호석유화학', 'AK홀딩스', '하이트진로홀딩스', '유진기업']}

groupList = [group19, group20]
api.groupList = groupList
myAPIKey = "7946dcde119af7656afc01157071c0ab9488b9ad"  # api key
api.apiKey = myAPIKey
# api.saveGroupListData()
# api.getCBDataAll()
api.getCBData('LG', '2019')
# api.getCBDataof(2019)


