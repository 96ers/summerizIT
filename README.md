# SummerizIT

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://github.com/tiangolo/fastapi)
[![React](https://img.shields.io/badge/React-005571?style=for-the-badge&logo=react)](https://reactjs.org/)

Đây là 1 tool cho phép người dùng có thể tóm tắt văn bản đầu vào ở dạng tiếng Anh và dịch văn bản đã tóm tắt đó sang tiếng Việt.

Report: 
- [Document](https://docs.google.com/document/d/1URkyuv_C2SSsYtNu5gWc6Z3dcwwfmbhed4w3-lTxEzs/edit?fbclid=IwZXh0bgNhZW0CMTAAAR0eUyu2_G6jwXAX4kW2zOHcpEkP92G9ykkpEhIpxeOxVAlvLHDSvQjt2dA_aem_AYHzMUGWYPekvqyKVZdzHXUVkAvS30fK4nhSMRLY-uyK7chF_Pt1L5lGPs3rpIreN_fDw39QyqdwNhahnWhSTVGe#heading=h.12nop7awgiff)


- [Video](https://drive.google.com/drive/folders/1Q_DyHPz0xmShHvHyOr_PPgryo1ul51JM?usp=sharing)
# Table of contents

1. [Giới thiệu](#summerizIT)

2. [Công nghệ](#tech-stack)
3. [Kiến thức nhận được](#lessons-learned)
4. [Triển khai các components trong phần mềm](#deploy-components)
   1. [Server](server/README.md)
   2. [Client](client/README.md)
   3. [ML models](#deploy-components)
5. [Acknowledgements](#acknowledgements)
6. [License](#license)

## Screenshots

[![app-screenshot.png](https://i.postimg.cc/8CS5CwTc/app-screenshot.png)](https://postimg.cc/rDfcn102)
## Tech Stack

**Client:** React, TailwindCss, React-redux

**Server:** FastAPI
## Lessons Learned

- Cách xây dựng một phần mềm
- Cách sử dụng các thuật toán AI trong việc giải quyết vấn đề cụ thể trong 1 dự án phần mềm
- Cách tổ chức và hoạt động nhóm 
- Áp dụng các kiến thức đã học vào một dứ án thực tế

## Deploy components

Clone the project

```bash
git clone https://github.com/96ers/summerizIT.git
```

Go to the project directory

```bash
cd summerizIT
```

1. Server
Xem tại [đây](server/README.md)

2. Client
Xem tại [đây](client/README.md)

3. ML models
```bash
cd MLmodels
pip install -r requirements.txt
python server.py
```

## Acknowledgements
- [FastAPI wonder Framework](https://fastapi.tiangolo.com/)
- [React + Vite + Tailwind](https://vitejs.dev/guide/)
- [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)



## License

[MIT](LICENSE)
