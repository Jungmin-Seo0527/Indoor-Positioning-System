# Indoor Positioning System

## 프로젝트 개요

* 비콘에서 송신하는 RSSI값을 이용해서 실내 측위를 하는 시스템
* RSSI의 낮은 신뢰성, 방향성이 없는 단점을 딥러닝을 적용하여 개선

## 프로젝트 실행

* `Main.py` 실행

### 1. 메인 화면

![](https://i.ibb.co/vPj9Krp/image.jpg)

* 건물 구조 보기
    * 가상의 실내 공간의 구조를 보여줍니다.
      ![](https://i.ibb.co/Wxgp4Cs/image.jpg)
        * 2층 건물이며 각 층에는 8개의 방이 존재, 중앙에 복도가 존재
        * 빨간점이 비콘을 의미합니다.
        * 거리의 단위는 미터 입니다. (40m X 20m X 6m)

* 한 층의 평면도 보기
    * 건물 구조의 단층 이미지를 보여줍니다.
      ![](https://i.ibb.co/CvKdP06/image.jpg)
        * 좌측이 일층, 우측이 2층 입니다.
        * 각 층에는 8개의 방이 존재하며, 중앙에는 복도가 있습니다.

* 딥러닝 모델 보기
    * 개발한 딥러닝 모델의 구조 이미지 입니다.
      ![](https://i.ibb.co/WBg3fHM/image.jpg)
        * 건물에 존재하는 총 18개의 비콘에서 송신하는 RSSI값을 입력받아서 Hidden Layer를 거쳐서 (x, y, z)좌표인 3개의 Output을 도출해내는 DNN(Deep Neural
          Network) 구조로 개발하였습니다.

### 2. 러닝된 데이터 불러오기 (테스트 케이스와 임의의 좌표 입력)

