clip_length = 16
ssd_input_shape = (300, 300, 3)
c3d_input_shape = (112, 112, clip_length, 3)
cnn2d_ImW = 64
cnn2d_ImH = 64
cnn_2d_input_shape = (cnn2d_ImH, cnn2d_ImW, 3)
winWidth = 640
winHeight = 480
mode = 'crop'
action_classes = ['standing', 'walking', 'sitting']
pose_classes = ['stand', 'sit', 'bend', 'squat']