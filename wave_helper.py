import sys

global saved_data
global saved_fs
saved_data = "Not saved yet"
saved_fs = "Not saved yet"

stps = {
    "increase_volume_site_example": {
        "wave_fs": 2200,
        "wave_data": [[-32760, -100], [-55, -55], [0, 0], [4, -2017], [32767, 10002]],
        "res_data": [[-32768, -120], [-66, -66], [0, 0], [4, -2420], [32767, 12002]],
        "res_fs": 2200,
        "input": "1\no.wav\n4\n1\nf.wav\n4\n"
    },

    "increase_volume_integer_only": {
        "wave_fs": 2200,
        "wave_data": [[10, -10], [0, 0]],
        "res_data": [[12, -12], [0, 0]],
        "res_fs": 2200,
        "input": "1\no.wav\n4\n1\nf.wav\n4\n"
    },

    "increase_volume_empty_list": {
        "wave_fs": 2200,
        "wave_data": [],
        "res_data": [],
        "res_fs": 2200,
        "input": "1\no.wav\n4\n1\nf.wav\n4\n"
    },

    "increase_volume_out_of_bounds": {
        "wave_fs": 2200,
        "wave_data": [[100, -10], [0, 0], [32766, -32767]],
        "res_data": [[120, -12], [0, 0], [32767, -32768]],
        "res_fs": 2200,
        "input": "1\no.wav\n4\n1\nf.wav\n4\n"
    },

    "decrease_volume_site_exmaple": {
        "wave_fs": 2200,
        "wave_data": [[-32760, -100], [-55, -55], [0, 0], [4, -2017], [32767, 10002]],
        "res_data": [[-27300, -83], [-45, -45], [0, 0], [3, -1680], [27305, 8335]],
        "res_fs": 2200,
        "input": "1\no.wav\n5\n1\nf.wav\n4\n"
    },

    "decrease_volume_empty_list": {
        "wave_fs": 2200,
        "wave_data": [[-32760, -100], [-55, -55], [0, 0], [4, -2017], [32767, 10002]],
        "res_data": [[-27300, -83], [-45, -45], [0, 0], [3, -1680], [27305, 8335]],
        "res_fs": 2200,
        "input": "1\no.wav\n5\n1\nf.wav\n4\n"
    },

    "speed_up_empty_list": {
        "wave_fs": 2200,
        "wave_data": [],
        "res_data": [],
        "res_fs": 2200,
        "input": "1\no.wav\n2\n1\nf.wav\n4\n"
    },

    "speed_up_site_exmaple": {
        "wave_fs": 2200,
        "wave_data": [[1,1], [2,2], [3,3], [4,4], [5,5]],
        "res_data": [[1,1], [3,3], [5,5]],
        "res_fs": 2200,
        "input": "1\no.wav\n2\n1\nf.wav\n4\n"
    },

    "speed_up_even_length": {
        "wave_fs": 2200,
        "wave_data": [[1,1], [2,2]],
        "res_data": [[1,1]],
        "res_fs": 2200,
        "input": "1\no.wav\n2\n1\nf.wav\n4\n"
    },

    "slow_down_empty_list": {
        "wave_fs": 2200,
        "wave_data": [],
        "res_data": [],
        "res_fs": 2200,
        "input": "1\no.wav\n3\n1\nf.wav\n4\n"
    },

    "slow_down_list_of_one": {
        "wave_fs": 2200,
        "wave_data": [[1,1]],
        "res_data": [[1,1]],
        "res_fs": 2200,
        "input": "1\no.wav\n3\n1\nf.wav\n4\n"
    },

    "slow_down_site_example": {
        "wave_fs": 2200,
        "wave_data": [[10,10], [20,30], [30,50], [40, 60]],
        "res_data": [[10,10], [15, 20], [20,30], [25, 40], [30,50], [35, 55], [40, 60]],
        "res_fs": 2200,
        "input": "1\no.wav\n3\n1\nf.wav\n4\n"
    },

    "reverse_empty_list": {
        "wave_fs": 2200,
        "wave_data": [],
        "res_data": [],
        "res_fs": 2200,
        "input": "1\no.wav\n1\n1\nf.wav\n4\n"

    },

    "reverse_site_example": {
        "wave_fs": 2200,
        "wave_data": [[1,1], [2,2], [3,3], [4,4]],
        "res_data": [[4,4], [3,3], [2,2], [1,1]],
        "res_fs": 2200,
        "input": "1\no.wav\n1\n1\nf.wav\n4\n"
    },

    "lowpass_empty_list": {
        "wave_fs": 2200,
        "wave_data": [],
        "res_data": [],
        "res_fs": 2200,
        "input": "1\no.wav\n6\n1\nf.wav\n4\n"
    },

    "lowpass_site_example": {
        "wave_fs": 2200,
        "wave_data": [[1, 1], [7, 7], [20, 20], [9, 9], [-12, -12]],
        "res_data": [[4, 4], [9, 9], [12, 12], [5, 5], [-1, -1]],
        "res_fs": 2200,
        "input": "1\no.wav\n6\n1\nf.wav\n4\n"
    },

    "lowpass_list_of_one": {
        "wave_fs": 2200,
        "wave_data": [[1, 1]],
        "res_data": [[1,1]],
        "res_fs": 2200,
        "input": "1\no.wav\n6\n1\nf.wav\n4\n"

    },

    "increase_reverse": {
        "wave_fs": 2200,
        "wave_data": [[1,1], [2,2], [3,3], [4,4], [5,5]],
        "res_data": [[5,5], [3,3], [1,1]],
        "res_fs": 2200,
        "input": "1\no.wav\n2\n2\n1\n1\nf.wav\n4\n"
    },

    "invalid_actions": {
        "wave_fs": 2200,
        "wave_data": [[1, 1]],
        "res_data": [[1,1]],
        "res_fs": 2200,
        "input": "a\n5\n1\no.wav\n1\n1\n3\nf.wav\n5\n4\n"
    },

    "merge1": {
        "need_i": True,
        "wave_fs": [2200, 2200],
        "wave_data": [
            [[1, -1], [2, -2], [3, -3], [4, -4]],
            [[20, -40], [2, 0], [-50, 7], [30150, -200]]
        ],
        "res_fs": 2200,
        "res_data": [[10, -20], [2, -1], [-23, 2], [15077, -102]],
        "input": "2\no.wav o2.wav\n1\nf.wav\n4\n"

    },

    "merge2": {
        "need_i": True,
        "wave_fs": [2200, 2200],
        "wave_data": [
            [[20, 20], [40, 40], [60, 60]],
            [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]]

        ],
        "res_fs": 2200,
        "res_data": [[10, 10], [21, 21], [32, 32], [7, 7], [9, 9]],
        "input": "2\no.wav o2.wav\n1\nf.wav\n4\n"

    },

    "merge3": {
        "need_i": True,
        "wave_fs": [2200, 5500],
        "wave_data": [
            [[0, 0], [0, 0], [0, 0], [0, 0]],
            [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]

        ],
        "res_fs": 2200,
        "res_data": [[5, 5], [10, 10], [30, 30], [35, 35]],
        "input": "2\no.wav o2.wav\n1\nf.wav\n4\n"

    },


    "merge4": {
        "need_i": True,
        "wave_fs": [2, 3],
        "wave_data": [
            [[20, 20], [40, 40], [60, 60], [80, 80], [100, 100]],
            [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19]]

        ],
        "res_fs": 2,
        "res_data": [[10, 10], [21, 21], [33, 33], [44, 44], [56, 56], [15, 15], [19, 19]],
        "input": "2\no.wav o2.wav\n1\nf.wav\n4\n"

    },

}


global tlp_setup
global data_i
global need_i
tlp_setup = "increase_volume_site_example"
data_i = 0
need_i = False


def set_setup(name):
    global tlp_setup
    global need_i
    global data_i
    global saved_data
    global saved_fs

    saved_data = "Not saved yet"
    saved_fs = "Not saved yet"

    tlp_setup = name
    need_i = False
    data_i = 0

    if ('need_i') in stps[tlp_setup].keys():
        need_i = True



def load_wave(wave_filename):
    wave_data = wave_fs = None
    global data_i


    if not need_i:
        wave_data = stps[tlp_setup]["wave_data"]
        wave_fs = stps[tlp_setup]["wave_fs"]

    else:
        wave_data = stps[tlp_setup]["wave_data"][data_i]
        wave_fs = stps[tlp_setup]["wave_fs"][data_i]

        data_i += 1

    return wave_fs, wave_data


def save_wave(frame_rate, audio_data, wave_filename):
    global saved_data
    global saved_fs

    saved_data = audio_data
    saved_fs = frame_rate
