=========================================================
���� �ϴ� ����� �����ش� => 0_TRAIN_TENSOR ���� 

���̽��� ������ġ ���Ѵ� => 0_ESTIMATING_POSITION_temp ���� (case n���� n��°�� case ����)
(train_model3.ckpt-n n�� ���� ���° epoch���� ���ð���)

�������� RSSI�� ������ġ�� �׷����� ���� => 0_visualize_map_temp_case1 ���� (�����̸����� ��������)

�ǹ� ������ ������ġ�� �����ش� => 0_watch_where (��ġ�� ���ο� �ִ� ��ǥ�� ����)

------------------------------------------------------------------------------------------
<<<<<<<<<<input�� �ϴ°��>>>>>>>>>>

input���� ���� ��ġ�� �ش� ��ġ�� ��Ī�Ǵ� �������� �����ϴ� �Լ� => inputing (���ο� �ִ� ��ǥ�� ��ġ����)

�������� �Է¹޾� ��ġ�����ϴ� �Լ� => ESTIMATING_POSITION_temp_for_inputing(���ϰ��� ��ġ)

�̰� ���� �ڵ� => Watch

�ǹ������� ������ġ�� �����ش� => watch_where_func

�̰ɺ����ڵ� =>  testy

&&&&&&&&&�������� RSSI�� ������ġ�� �׷����� ���� : �̰� nano power�� ���� ����ؾ��ؼ� �����̴�&&&&&&&&&&

==========================================================
<<<<<<<<<<����>>>>>>>>>>

0_TRAIN_TENSOR : �̰ɷ� �����ϴ°�
('txt2py_x_data.txt','txt2py_y_data.txt')

way_2_reload : 0_ESTIMATING_POSITION, 0_visualize_map ���� ����
(0_ESTIMATING_POSITION, 0_visualize_map,reloading_func)

reloading_func : ���� open �Լ�

0_visualize_map_temp_case5 : ��ȣ���� ǥ�� �����ִ� �ڵ�
('txt2py_map_1_data_case5_for_map.txt','txt2py_map_2_data_case5_for_map.txt')

mola : 3D �׷��� �����ִ� �Լ�

0_watch_where :  ��ġ ��������� �����ִ� �ڵ�  // �Լ��� �����ؾ��ҵ�
(mola)

0_ESTIMATING_POSITION_temp : ��ġ���� �ڵ�
('txt2py_map_1_data_case5_for_map.txt','txt2py_map_2_data_case5_for_map.txt', module2,train_model3.ckpt-500)

module2 : cell ������ �ڵ�

train_model3.ckpt-500 : save and restore, tensorboard �ڷ�

ROUNDING : �Է� ��ǥ �ٷ�� �Լ�

ESTIMATINGSIGNAL : ��ġ�� ���� �ش��ϴ� ���������� ��Ī�ϴ� �Լ�
(ROUNDING, module2, 'txt2py_x_data_input_signal.txt', 'txt2py_y_data_input_position.txt')

testing : input ��ġ�� ���� ��ȣ���� �����ڵ�
(ESTIMATINGSIGNAL)

txt2py_y_data_input_position : input�� ���� ������ġ
txt2py_x_data_input_signal : txt2py_y_data_input_position�� ���� ��ȣ����

ESTIMATING_POSITION_temp_for_inputing : �Լ�, �Է� = ���Ž�ȣ����, ��°� = ��ǥ