# Updating
# I.Introduction:
    This is my personal use project

# II. Project components
- infrastructure : aws with `cdk` for IaC , handle everything except for SQL db which is supabase (totally free for now).

- runtime (`backend`): powered by `aws chalice` for both restful api and event-driven:
    endpoint : https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api
- kycoui (`frontend`):  reactjs (with nextjs), currently only export to static site and hosted on s3
    endpoint : https://dl4uq37pbr4d2.cloudfront.net/


Note:
- Database postgres: `superbase.com`  with postgres at https://app.supabase.com/project/xggbesitxdlxuygrlmjk
- Redis ? : updating
- ....

# III. Development

# IV. Usages
    - Register:
    `http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/v1/auth/register email=tranthanhbao_tester@gmail.com password=Abc123!@#`
    - Login:
    `http POST  https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/v1/auth/login email=tranthanhbao_tester@gmail.com password=Abc123!@#`
