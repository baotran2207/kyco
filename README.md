# Updating

# I.Introduction:

This is my personal use project

- endpoint : https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api
- api routes: https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/docs

# II. Project components

- infrastructure : aws with `cdk` for IaC , handle everything except for SQL db which is supabase (totally free for now).

- runtime (`backend`): powered by `aws chalice` for both restful api and event-driven:
  endpoint : https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api
- kycoui (`frontend`): reactjs (with nextjs), currently only export to static site and hosted on s3
  endpoint : https://dl4uq37pbr4d2.cloudfront.net/

Note:

- Database postgres: `superbase.com` with postgres at https://app.supabase.com/project/xggbesitxdlxuygrlmjk
- Redis ? : updating
- ....

# III. Development

# IV. Usages

1. Install [httpie](https://pypi.org/project/httpie/) for http request (it is more human friendly than curl):

`pip install httpie`

2. Replace `tranthanhbao_tester@gmail.com` with your test email
## A. Auth

- Register without/with password:

a. Without password

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/login email=tranthanhbao_tester@gmail.com `

b. With password

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/login email=tranthanhbao_tester@gmail.com password=Abc123!@#`



## B. Verify email

- Verify email:

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/verify_email email=tranthanhbao_tester@gmail.com  confirmation_code=282484`

- Resend confirmation code:

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/resend_confirmation email=tranthanhbao_tester@gmail.com `

## C. Login
Note:
- email must be verified before login (cognito requirement)
- Reponse: tokens

a.Login withn password:

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/login email=tranthanhbao_tester@gmail.com  password=Abc123!@#`

b.Login without password (via otp code)

- Request otp

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/init_challenge email=tranthanhbao_tester@gmail.com `


- Login with otp (otp code received from email and session_id = response from api `init_challenge`):

`http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/auth/login_with_challenge email=tranthanhbao_tester@gmail.com  challenge_answer=<otp_via_email> challenge_session_id=<response from init_challenge>`


[![login_with_otp.md.png](https://img.upanh.tv/2023/08/01/login_with_otp.md.png)](https://upanh.tv/image/jXVrJF)