=========================================================
러닝 하는 모습을 보여준다 => 0_TRAIN_TENSOR 실행 

케이스별 추정위치 구한다 => 0_ESTIMATING_POSITION_temp 실행 (case n으로 n번째의 case 설정)
(train_model3.ckpt-n n에 따라 몇번째 epoch인지 선택가능)

센서별의 RSSI와 추정위치를 그래프로 본다 => 0_visualize_map_temp_case1 실행 (파일이름별로 나눠있음)

건물 구조와 추정위치를 보여준다 => 0_watch_where (위치는 내부에 있는 좌표로 설정)

------------------------------------------------------------------------------------------
<<<<<<<<<<input을 하는경우>>>>>>>>>>

input으로 정한 위치와 해당 위치에 매칭되는 센서값을 도출하는 함수 => inputing (내부에 있는 좌표로 위치선정)

센서값을 입력받아 위치추정하는 함수 => ESTIMATING_POSITION_temp_for_inputing(리턴값이 위치)

이걸 보는 코드 => Watch

건물구조와 추정위치를 보여준다 => watch_where_func

이걸보는코드 =>  testy

&&&&&&&&&센서별의 RSSI와 추정위치를 그래프로 본다 : 이게 nano power를 직접 계산해야해서 문제이다&&&&&&&&&&

==========================================================
<<<<<<<<<<설명>>>>>>>>>>

0_TRAIN_TENSOR : 이걸로 러닝하는거
('txt2py_x_data.txt','txt2py_y_data.txt')

way_2_reload : 0_ESTIMATING_POSITION, 0_visualize_map 파일 실행
(0_ESTIMATING_POSITION, 0_visualize_map,reloading_func)

reloading_func : 파일 open 함수

0_visualize_map_temp_case5 : 신호세기 표로 보여주는 코드
('txt2py_map_1_data_case5_for_map.txt','txt2py_map_2_data_case5_for_map.txt')

mola : 3D 그래픽 보여주는 함수

0_watch_where :  위치 졸라맨으로 보여주는 코드  // 함수로 변경해야할듯
(mola)

0_ESTIMATING_POSITION_temp : 위치추정 코드
('txt2py_map_1_data_case5_for_map.txt','txt2py_map_2_data_case5_for_map.txt', module2,train_model3.ckpt-500)

module2 : cell 나누는 코드

train_model3.ckpt-500 : save and restore, tensorboard 자료

ROUNDING : 입력 좌표 다루는 함수

ESTIMATINGSIGNAL : 위치에 따른 해당하는 센서값들을 매칭하는 함수
(ROUNDING, module2, 'txt2py_x_data_input_signal.txt', 'txt2py_y_data_input_position.txt')

testing : input 위치에 따른 신호세기 실행코드
(ESTIMATINGSIGNAL)

txt2py_y_data_input_position : input에 따른 수정위치
txt2py_x_data_input_signal : txt2py_y_data_input_position에 따른 신호세기

ESTIMATING_POSITION_temp_for_inputing : 함수, 입력 = 수신신호세기, 출력값 = 좌표