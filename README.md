# Django와 Slack 이벤트 API를 활용한 예제

이 프로젝트는 Django를 사용하여 Slack 이벤트를 처리하고 특정 메시지에 응답하는 간단한 애플리케이션 예제이다. Slack Events API를 통해 들어오는 요청을 처리하고, 지정된 키워드에 따라 Slack 채널에 메시지를 전송하는 기능을 포함한다.

## 주요 기능

1. **Slack 이벤트 처리**  
   - Slack으로부터 전달된 이벤트 데이터를 Django REST Framework를 통해 처리.  
   - URL 검증을 위한 Slack의 `challenge` 요청을 처리.

2. **메시지 응답**  
   - Slack 채널에서 특정 키워드(`hello`)가 포함된 메시지를 감지하여 자동으로 응답(`hello_slack!`)을 전송.

3. **Slack API 연동**  
   - Slack의 `chat.postMessage` API를 사용하여 봇이 채널에 메시지를 보낼 수 있다.  
   - 봇 토큰은 환경 변수(`SLACK_BOT_TOKEN`)를 통해 안전하게 관리.

## 설정 및 실행 방법

1. **Slack 앱 생성**  
   - [Slack API](https://api.slack.com/)에서 새로운 앱을 생성.  
   - 이벤트 구독(Event Subscriptions)을 활성화하고, 이 애플리케이션의 엔드포인트 URL을 등록.  
   - 처리할 이벤트(`message.channels`)를 추가.  

2. **환경 변수 설정**  
   - Slack 봇 토큰을 환경 변수 `SLACK_BOT_TOKEN`에 설정.


## 테스트
- 메시지 전송 테스트:
  - Slack 채널에서 봇이 추가된 후 `"hello"`라는 단어가 포함된 메시지를 보내면, 봇이 `"hello_slack!"`이라는 응답을 전송합니다.

