
# json api란?


넓게는 JSON 포맷으로 통신하는 모든 API를 뜻하지만, 좁은 의미로는 `jsonapi.org` 에서 정의한 '데이터 교환 표준 스펙

단순히 데이터를 주고받는 것을 넘어, **리소스 간의 관계(Relationships)를 표현**하고, 요청 횟수를 줄이는(Compound Documents) 등 효율적인 통신을 위한 **엄격한 규칙**을 따르는 API

왜 엄격한 규칙?

데이터 전송시 구조가 규칙으로 정해져 있음

비교

일반 API (구조가 달라질 수 있음)

``` json
// 유저 응답 
{
  "user": { "name": "철수", "age": 25 },
  "status": "OK"
}

// 상품 응답 
{
  "items": [
    { "productName": "노트북", "price": 1000000 }
  ],
  "message": "성공"
}
```


json api

데이터는 무조건 data안에 속성은 attributes 안에 넣음

```json
// 유저 응답
{
  "data": {
    "type": "users",
    "id": "1",
    "attributes": {
      "name": "철수", // <-- 이름이 여기 있음
      "age": 25
    }
  }
}

// 상품 응답
{
  "data": {
    "type": "products",
    "id": "100",
    "attributes": {
      "name": "노트북", // <-- 이름이 똑같은 위치에 있음
      "price": 1000000
    }
  }
}
```

# 장점 

1. 코드 재사용성이 높다.
	데이터 종류마다 파싱 코드를 짤필요 없이 하나의 함수로 파싱하는 데이터 대상만 바꾸면 됨

2. 'N+1 문제' 해결

	**n+1 문제란?**
	목록(1번)을 조회한 후, 각 데이터에 연관된 정보(프로필, 댓글 등)를 얻기 위해 데이터 개수만큼(N번) 추가적인 DB 쿼리를 반복해서 날리는 비효율적인 상황<br>
	1은 목록을 가져오는 최초의 쿼리, n은 목록의 데이터 갯수만큼 날린 쿼리문<br>
	json api는 이걸 include 파라미터로 해결한다
	\+ Compound Documents(복합문서)라 부름<br>
	- **기존 방식 (N+1 발생):** `GET /articles` (게시글만 줘) ➔ 나중에 작성자 정보 없어서 또 요청해야 함
    
	- **JSON API 방식 (해결!):** **`GET /articles?include=author`** (게시글 주면서 작성자도 같이 담음) ➔ **단 1번의 요청**으로 끝난다<br>
	예시
	- **`data`**: 요청한 **메인 데이터** (게시글)
    
	- **`included`**: 같이 달라고 한 **관련 데이터** (작성자)<br>
	```json
	{
  // 1. 메인 데이터 (게시글 목록)
  "data": [
    {
      "type": "articles",
      "id": "1",
      "attributes": { "title": "JSON API 학습법" },
      "relationships": {
        "author": {
          "data": { "type": "people", "id": "9" } // <-- "작성자는 9번이야"라고 가리킴
        }
      }
    },
    {
      "type": "articles",
      "id": "2",
      "attributes": { "title": "N+1 문제 해결" },
      "relationships": {
        "author": {
          "data": { "type": "people", "id": "9" } // <-- "이것도 9번이 썼음"
        }
      }
    }
  ],

  // 2. 포함된 데이터 (여기에 작성자 정보가 딱! 들어옴)
  "included": [
    {
      "type": "people",
      "id": "9", // <-- 위에서 가리킨 9번의 실체
      "attributes": {
        "name": "주니어개발자",
        "twitter": "@junior_dev"
      }
    }
  ]
}
	```
	
	
	이걸 활용해서 json api는 꼬리에 꼬리를 무는 데이터도 한번의 요청으로 가져올 수 있음
	
	- **요청:** `GET /articles?include=author,comments.author`
    
	- **의미:**
    
    1. 게시글 줘.
        
    2. 그 글 쓴 작성자(`author`)도 줘.
        
    3. 그 글의 댓글(`comments`)도 줘.
        
    4. 심지어 그 댓글을 쓴 사람(`comments.author`)까지 줘

# 단점

JSON API 스펙은 `data > attributes` 처럼 **중첩된 구조(Depth)가 강제**되기 때문에,

1. 일반적인 API보다 **데이터를 꺼내는 코드가 길어지고,
    
2. 중간에 데이터가 비어있을 경우 **참조 에러(Null Pointer Exception)로 인해 앱이 비정상 종료될 위험**이 높아진다.<br>
최근에는 json api의 단점을 보완하고자 GraphQL, Pragmatic REST 을 사용하기도 함



# 응답/요청 구조 설계 패턴<br>

## 1. Envelope 패턴<br>
데이터만 보내는게 아니라 항상 똑같은 구조에 담아서 보내는 방식

패턴 적용하기 전
```JSON
// 성공했을 때 (배열 반환)
[ { "id": 1, "name": "철수" } ]

// 실패했을 때 (객체 반환)
{ "message": "에러 발생!" }
```

패턴 적용후
```JSON
// 성공했을 때
{
  "status": "SUCCESS",
  "data": [ { "id": 1, "name": "철수" } ], // 데이터는 여기!
  "error": null
}

// 실패했을 때
{
  "status": "ERROR",
  "data": null,
  "error": { "code": "E400", "message": "잘못된 요청" } // 에러는 여기!
}
```


공통 응답 필드 (Response Wrapper)

| **필드명**         | **타입**         | **설명**                                |
| --------------- | -------------- | ------------------------------------- |
| **`result`**    | String / Enum  | 요청 결과 상태 (`SUCCESS`, `FAIL`, `ERROR`) |
| **`data`**      | Object / Array | 성공 시 실제 데이터 (실패 시 `null`)             |
| **`message`**   | String         | 사용자에게 보여줄 간단한 메시지 (선택 사항)             |
| **`errorCode`** | String         | 실패 시 에러 코드 (성공 시 `null`)              |

성공 응답시
data에 내용이 들어가고 에러 관련 필드는 비워둔다.

```json
{
  "result": "SUCCESS",
  "data": {
    "userId": 101,
    "username": "junior_dev",
    "email": "dev@example.com"
  },
  "message": null,     // 성공했으니 메시지 불필요 (또는 "조회 성공")
  "errorCode": null    // 에러 없으니까 null
}
```

에러 응답시
HTTP 상태 코드(400, 500)와 별개로 **구체적인 에러 사유**를 알려줘야 한다.

```json
{
  "result": "FAIL",
  "data": null,        // 실패했으니 데이터 없음
  "message": "이메일 형식이 올바르지 않습니다.", // 사용자에게 보여줄 메시지
  "errorCode": "USER_001_INVALID_EMAIL"     // 프론트엔드가 처리할 고유 코드
}
```


### 장점<br>
1) 응답 본문의 고정된 영역에 전체 페이지 수나 서버 시간 같은 부가 정보를 담을 수 있어, 데이터의 확장성이 뛰어나다.
   
2) 에러 처리를 획일화 할수 있다.
	http 상태 코드에만 의존하지 않고 비즈니스 로직 결과를 명확히 전달 가능, response.result 값을 확인해 `SUCCESS`면 -> 화면 갱신 `FAIL`이면 -> 에러 메시지 팝업

### 단점

1) 중간서버 캐싱 오류: 브라우저나 CDN이 에러 메시지를 포함한 `200 OK` 응답을 정상 데이터로 오인해 저장해버리면, 이후 사용자에게 계속해서 에러 화면이 노출될 수 있다.
   
2) 불필요한 데이터 낭비: 아주 작은 데이터를 보낼 때도 고정된 Envelope 규격(status, message 등)을 모두 포함해야 하므로 네트워크 트래픽 효율이 떨어질 수 있다.

## 2. Bare 패턴<br>
Envelope(봉투)이라는 개념 자체를 쓰지 않고 데이터만 바로 반환하는 가장 표준적인 REST 방식

응답의 최상위에 실제 데이터(객체나 배열)가 바로 나온다.


## 3. HATEOAS(헤이티오스) 패턴<br>
데이터와 함께 "이 데이터로 다음에 할 수 있는 행동(Link)"을 같이 알려주는 방식


## 4. BFF(Backend For Frontend) 패턴<br>
클라이언트 종류(웹, iOS, Android)에 따라 **서버가 응답 구조를 각각 다르게 다듬어서** 내려주는 패턴



**위 패턴들은 특정 포맷(JSON)에 종속된 것이 아니라 REST API 아키텍처 전반에 적용 가능한 설계이다.**

