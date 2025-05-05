<p align="center">
  <br/>
    <img alt="old_huggingface_hub library logo" src="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/old_huggingface_hub.svg" width="376" height="59" style="max-width: 100%;">
  <br/>
</p>

<p align="center">
    <i>공식 Huggingface Hub 파이썬 클라이언트</i>
</p>

<p align="center">
    <a href="https://huggingface.co/docs/old_huggingface_hub/ko/index"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/old_huggingface_hub/index.svg?down_color=red&down_message=offline&up_message=online&label=doc"></a>
    <a href="https://github.com/huggingface/old_huggingface_hub/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/old_huggingface_hub.svg"></a>
    <a href="https://github.com/huggingface/old_huggingface_hub"><img alt="PyPi version" src="https://img.shields.io/pypi/pyversions/old_huggingface_hub.svg"></a>
    <a href="https://pypi.org/project/old-huggingface-hub"><img alt="downloads" src="https://static.pepy.tech/badge/old_huggingface_hub/month"></a>
    <a href="https://codecov.io/gh/huggingface/old_huggingface_hub"><img alt="Code coverage" src="https://codecov.io/gh/huggingface/old_huggingface_hub/branch/main/graph/badge.svg?token=RXP95LE2XL"></a>
</p>

<h4 align="center">
    <p>
        <a href="https://github.com/huggingface/old_huggingface_hub/blob/main/README.md">English</a> |
        <a href="https://github.com/huggingface/old_huggingface_hub/blob/main/README_de.md">Deutsch</a> |
        <a href="https://github.com/huggingface/old_huggingface_hub/blob/main/README_hi.md">हिंदी</a> |
        <b>한국어</b>|
        <a href="https://github.com/huggingface/old_huggingface_hub/blob/main/README_cn.md">中文（简体）</a>
    <p>
</h4>

---

**기술 문서**: <a href="https://hf.co/docs/old_huggingface_hub" target="_blank">https://hf.co/docs/old_huggingface_hub</a>

**소스 코드**: <a href="https://github.com/huggingface/old_huggingface_hub" target="_blank">https://github.com/huggingface/old_huggingface_hub</a>

---

## old_huggingface_hub 라이브러리 개요

`old_huggingface_hub` 라이브러리는 [Hugging Face Hub](https://huggingface.co/)와 상호작용할 수 있게 해줍니다. Hugging Face Hub는 창작자와 협업자를 위한 오픈소스 머신러닝 플랫폼입니다. 여러분의 프로젝트에 적합한 사전 훈련된 모델과 데이터셋을 발견하거나, Hub에 호스팅된 수천 개의 머신러닝 앱들을 사용해보세요. 또한, 여러분이 만든 모델, 데이터셋, 데모를 커뮤니티와 공유할 수도 있습니다. `old_huggingface_hub` 라이브러리는 파이썬으로 이 모든 것을 간단하게 할 수 있는 방법을 제공합니다.

## 주요 기능

- Hub에서 [파일을 다운로드](https://huggingface.co/docs/old_huggingface_hub/main/ko/guides/download)
- Hub에 [파일을 업로드](https://huggingface.co/docs/old_huggingface_hub/main/en/guides/upload) (영어)
- [레포지토리를 관리](https://huggingface.co/docs/old_huggingface_hub/main/en/guides/repository) (영어)
- 배포된 모델에 [추론을 실행](https://huggingface.co/docs/old_huggingface_hub/main/en/guides/inference) (영어)
- 모델, 데이터셋, Space를 [검색](https://huggingface.co/docs/old_huggingface_hub/main/en/guides/search) (영어)
- [모델 카드를 공유](https://huggingface.co/docs/old_huggingface_hub/main/en/guides/model-cards)하여 모델을 문서화 (영어)
- PR과 댓글을 통해 [커뮤니티와 소통](https://huggingface.co/docs/old_huggingface_hub/main/en/guides/community) (영어)

## 설치

[pip](https://pypi.org/project/old-huggingface-hub/)로 `old_huggingface_hub` 패키지를 설치하세요:

```bash
pip install old_huggingface_hub
```

원한다면 [conda](https://huggingface.co/docs/old_huggingface_hub/ko/installation#install-with-conda)를 이용하여 설치할 수도 있습니다.

기본 패키지를 작게 유지하기 위해 `old_huggingface_hub`는 유용한 의존성을 추가적으로 제공합니다. 추론과 관련된 기능을 원한다면, 아래를 실행하세요:

```bash
pip install old_huggingface_hub[inference]
```

설치와 선택적 의존성에 대해 더 알아보려면, [설치 가이드](https://huggingface.co/docs/old_huggingface_hub/ko/installation)를 참고하세요.

## 맛보기

### 파일 다운로드

파일 하나의 경우:

```py
from old_huggingface_hub import hf_hub_download

hf_hub_download(repo_id="tiiuae/falcon-7b-instruct", filename="config.json")
```

레포지토리 전체의 경우:

```py
from old_huggingface_hub import snapshot_download

snapshot_download("stabilityai/stable-diffusion-2-1")
```

파일은 로컬 캐시 폴더에 다운로드됩니다. 자세한 내용은 [이 가이드](https://huggingface.co/docs/old_huggingface_hub/ko/guides/manage-cache)를 참조하세요.

### 로그인

Hugging Face Hub는 토큰을 사용하여 애플리케이션을 인증합니다([문서](https://huggingface.co/docs/hub/security-tokens) 참조). 컴퓨터에서 로그인하려면 CLI를 사용하세요:

```bash
huggingface-cli login
# 또는 환경 변수로 지정해주세요
huggingface-cli login --token $HUGGINGFACE_TOKEN
```

### 레포지토리 생성

```py
from old_huggingface_hub import create_repo

create_repo(repo_id="super-cool-model")
```

### 파일 업로드

파일 하나의 경우:

```py
from old_huggingface_hub import upload_file

upload_file(
    path_or_fileobj="/home/lysandre/dummy-test/README.md",
    path_in_repo="README.md",
    repo_id="lysandre/test-model",
)
```

레포지토리 전체의 경우:

```py
from old_huggingface_hub import upload_folder

upload_folder(
    folder_path="/path/to/local/space",
    repo_id="username/my-cool-space",
    repo_type="space",
)
```

자세한 내용은 [업로드 가이드](https://huggingface.co/docs/old_huggingface_hub/ko/guides/upload)를 참조하세요.

## Hugging Face Hub와 함께 성장하기

저희는 멋진 오픈소스 ML 라이브러리들과 협력하여, 모델 호스팅과 버전 관리를 무료로 제공하고 있습니다. 이미 통합된 라이브러리들은 [여기](https://huggingface.co/docs/hub/libraries)서 확인할 수 있습니다.

이렇게 하면 다음과 같은 장점이 있습니다:

- 라이브러리 사용자들의 모델이나 데이터셋을 무료로 호스팅해줍니다.
- git을 기반으로 한 방식으로, 아주 큰 파일들도 버전을 관리할 수 있습니다.
- 공개된 모든 모델에 대해 추론 API를 호스팅해줍니다.
- 업로드된 모델들을 브라우저에서 쉽게 사용할 수 있는 위젯을 제공합니다.
- 누구나 여러분의 라이브러리에 새로운 모델을 업로드할 수 있습니다. 모델이 검색될 수 있도록 해당 태그만 추가하면 됩니다.
- 다운로드 속도가 매우 빠릅니다! 왜냐하면 Cloudfront (CDN)를 이용하여 전 세계 어디에서나 빠르게 다운로드할 수 있도록 지역적으로 복제해뒀기 때문입니다.
- 사용 통계와 더 많은 기능들을 제공합니다.

여러분의 라이브러리를 통합하고 싶다면, 이슈를 열어서 의견을 나눠주세요. 통합 과정을 안내하기 위해 ❤️을 담아 [단계별 가이드](https://huggingface.co/docs/hub/adding-a-library)를 작성했습니다.

## (기능 요청, 버그 패치 등의) 기여는 대환영입니다 💙💚💛💜🧡❤️

모든 분들의 기여를 환영하며, 소중히 생각합니다. 코드 작성만이 커뮤니티에 도움을 주는 유일한 방법이 아니에요.
질문에 답하거나, 다른 분들을 돕거나, 컨택하거나, 문서를 개선하는 것도 커뮤니티에 큰 도움이 됩니다.
지금 시작하려면 간단한 [기여 가이드](https://github.com/huggingface/old_huggingface_hub/blob/main/CONTRIBUTING.md)를 참조해주세요.
