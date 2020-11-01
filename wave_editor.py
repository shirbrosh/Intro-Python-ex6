from wave_helper import *
import math

CHANGE_ACTION_MSG = "Choose a change to preform:\n 1.revere\n 2.speed " \
                    "acceleration\n 3.speed deceasing\n 4.volume turn up\n 5." \
                    "volume turn down\n 6.low_pass_filter"
ACTION_MSG = "Choose number of action:\n 1.change wav file\n 2.combine 2 wav " \
             "files\n 3.composing melody in wav file format\n 4.exit program\n"
PASS_MENU_MSG = "Choose number of action:\n 1.save audio\n 2.change audio"
FAIL_MSG = "There was a problem with the inputs, please enter again"
COMBINE_FILES_MSG = "Please enter 2 file names and paths to combine in the " \
                    "following format:\n <file1_path><file2_path>"
MAX_RANGE = 32767
MIN_RANGE = -32768
SAMPLE_RATE = 2000
AUDIO_SAMPLES = 125
ERROR = -1


def reverse(audio_data):
    """A function that receives a list of lists and returns a new list
    containing the lists from the original list in reversed order"""
    return audio_data[::-1]


def speed_acceleration(audio_data):
    """A function that receives a list of lists and returns a new list
    containing only the lists that have even indexes"""
    return audio_data[::2]


def speed_deceasing(audio_data):
    """A function that receives a list of lists and returns a new list
    containing the original lists from the big list and between every original
    list there is a new list composed from the average of the lists before and
    after her"""
    new_audio_data = []
    for i in range(0, len(audio_data) - 1):
        new_audio_data.append(audio_data[i])
        avg_left = int((audio_data[i][0] + audio_data[i + 1][0]) / 2)
        avg_right = int((audio_data[i][1] + audio_data[i + 1][1]) / 2)
        avg = [avg_left, avg_right]
        new_audio_data.append(avg)
    new_audio_data.append(audio_data[len(audio_data) - 1])
    return new_audio_data


def volume_turn_up_or_down(audio_data, sign):
    """A function that receives a list of lists and returns a new list
    containing the original values times 1.2 or divide by 1.2 depend on the
    users input"""
    new_audio_data = []
    for lst in audio_data:
        new_audio_data_row = []
        for i in range(0, 2):
            if sign == "*":
                value = int(lst[i] * 1.2)
            elif sign == "/":
                value = int(lst[i] / 1.2)
            if value > MAX_RANGE:
                value = MAX_RANGE
            elif value < MIN_RANGE:
                value = MIN_RANGE
            new_audio_data_row.append(value)
        new_audio_data.append(new_audio_data_row)
    return new_audio_data


def low_pass_filter(audio_data):
    """A function that receives a list of lists and returns a new list
    containing the average of the value, the one before him and the one after
    him for each value in the original list """
    new_audio_data = []
    for i in range(0, len(audio_data)):
        if i == 0:
            value_left = int((audio_data[i][0] + audio_data[i + 1][0]) / 2)
            value_right = int((audio_data[i][1] + audio_data[i + 1][1]) / 2)
        elif i == len(audio_data) - 1:
            value_left = int((audio_data[i][0] + audio_data[i - 1][0]) / 2)
            value_right = int((audio_data[i][1] + audio_data[i - 1][1]) / 2)
        else:
            value_left = int((audio_data[i][0] + audio_data[i + 1][0] +
                              audio_data[i - 1][0]) / 3)
            value_right = int((audio_data[i][1] + audio_data[i + 1][1] +
                               audio_data[i - 1][0]) / 3)
        new_audio_data.append([value_left, value_right])
    return new_audio_data


def change_wav_file(audio_data=ERROR, frame_rate=ERROR):
    """A function that operates the change file menu, and changes the file
    according to the users input"""
    while audio_data == ERROR:
        file_name = input("Write the name of the file to edit")
        audio_data_load = load_wave(file_name)
        audio_data = audio_data_load[1]
        frame_rate = audio_data_load[0]
        if audio_data != ERROR:
            break
        else:
            print("There is a problem with the file")
    action = input(CHANGE_ACTION_MSG)
    if action == "1":
        audio_data_change = reverse(audio_data)
    elif action == "2":
        audio_data_change = speed_acceleration(audio_data)
    elif action == "3":
        audio_data_change = speed_deceasing(audio_data)
    elif action == "4":
        audio_data_change = volume_turn_up_or_down(audio_data, "*")
    elif action == "5":
        audio_data_change = volume_turn_up_or_down(audio_data, "/")
    elif action == "6":
        audio_data_change = low_pass_filter(audio_data)
    pass_menu(audio_data_change, frame_rate)


def combine_equal_len_and_rate(audio_data1, audio_data2):
    """A function that combines two audios data that has the same length and
    frame rate, the new audio data will be the average of each value from the
    original values"""
    combine_audio_data = []
    for j in range(0, len(audio_data1)):
        combine_audio_data_pair = []
        for i in range(0, 2):
            value = int((audio_data1[j][i] + audio_data2[j][i]) / 2)
            combine_audio_data_pair.append(value)
        combine_audio_data.append(combine_audio_data_pair)
    return combine_audio_data


def combine_equal_rate_not_len(longest_audio_data, shortest_audio_data):
    """A function that combines two audios data that has the same frame rate
    but different length, the new audio data will be the average of each value
    from the original values and then the extra values left in the longest
    audio data will be added"""
    combine_audio_data = combine_equal_len_and_rate(shortest_audio_data,
                                                    longest_audio_data)
    difference = len(longest_audio_data) - len(shortest_audio_data)
    for i in range(len(longest_audio_data) - difference,
                   len(longest_audio_data)):
        combine_audio_data.append(longest_audio_data[i])
    return combine_audio_data


def create_new_audio_by_rate(long_rate_audio_data, long_frame_rate,
                             short_frame_rate):
    """A function that create new audio data for the longer frame rate- creates
    new list composed only from the (short frame rate/ gc) values from each
    (long frame rate / gcd) values"""
    gc = int(math.gcd(long_frame_rate, short_frame_rate))
    num_longest_sample = int(long_frame_rate / gc)
    num_short_sample = int(short_frame_rate / gc)
    new_long_audio = []
    n = 1
    counter = 0
    for i in range(0, len(long_rate_audio_data)):
        if not num_short_sample + (num_longest_sample * (
                n - 1)) < i + 1 <= num_longest_sample * n:
            new_long_audio.append(long_rate_audio_data[i])
        counter += 1
        if counter == num_longest_sample:
            counter = 0
            n += 1
    return new_long_audio


def combine_audio(long_rate_audio_data, short_rate_audio_data,
                  long_frame_rate, short_frame_rate):
    """A function that combines two audios according to their length and frame
    rates"""
    new_long_audio = create_new_audio_by_rate(long_rate_audio_data,
                                              long_frame_rate,
                                              short_frame_rate)
    if len(new_long_audio) == len(short_rate_audio_data):
        result = combine_equal_len_and_rate(new_long_audio,
                                            short_rate_audio_data)
    elif len(new_long_audio) > len(short_rate_audio_data):
        result = combine_equal_rate_not_len(new_long_audio,
                                            short_rate_audio_data)
    else:
        result = combine_equal_rate_not_len(short_rate_audio_data,
                                            new_long_audio)
    return result


def combine_files_menu():
    """A function that asks for 2 file names to combine and operates the
    combine functions"""
    file_names = input(COMBINE_FILES_MSG)
    file_name_list = file_names.split()
    audio_data1 = load_wave(file_name_list[0])
    audio_data2 = load_wave(file_name_list[1])
    while audio_data1 == -1 or audio_data2 == -1:
        print("There is a problem with the files, please re-enter")
        file_names = input(COMBINE_FILES_MSG)
        file_name_list = file_names.split()
        audio_data1 = load_wave(file_name_list[0])
        audio_data2 = load_wave(file_name_list[1])
    frame_rate1 = audio_data1[0]
    frame_rate2 = audio_data2[0]
    if frame_rate1 > frame_rate2:
        combine_audio_data = combine_audio(audio_data1[1], audio_data2[1],
                                           frame_rate1, frame_rate2)
        pass_menu(combine_audio_data, frame_rate2)
    else:
        combine_audio_data = combine_audio(audio_data2[1], audio_data1[1],
                                           frame_rate2, frame_rate1)
        pass_menu(combine_audio_data, frame_rate1)


def frequency_by_letter(note):
    """A function that receives a note and returns its frequency"""
    if note == "A":
        frequency = 440
    elif note == "B":
        frequency = 494
    elif note == "C":
        frequency = 523
    elif note == "D":
        frequency = 587
    elif note == "E":
        frequency = 659
    elif note == "F":
        frequency = 698
    elif note == "G":
        frequency = 784
    elif note == "Q":
        frequency = 0
    return frequency


def composing_calculate(note, time):
    """A function that receives a note and play time and returns the matching
    audio data list according to the formula"""
    composing_for_letter = []
    frequency = frequency_by_letter(note)
    if frequency != 0:
        samples_per_cycle = SAMPLE_RATE / frequency
    for i in range(0, AUDIO_SAMPLES * time):
        if frequency != 0:
            value = int(
                MAX_RANGE * math.sin(math.pi * 2 * (i / samples_per_cycle)))
        else:
            value = 0
        audio_pairs = [value, value]
        composing_for_letter.append(audio_pairs)
    return composing_for_letter


def read_composing_file(filename):
    """A function that receives the composing file and returns a list of all
    the values"""
    file_name_open = open(filename)
    file_name_string = file_name_open.read()
    file_name_string_no_enter = file_name_string.strip()
    list_letters_time = file_name_string_no_enter.split()
    file_name_open.close()
    return list_letters_time


def composing():
    """A function that asks for instruction file name and creates the audio
    data according to the instructions"""
    final_composing = []
    filename = input("Please enter file name of composing instruction")
    list_letters_time = read_composing_file(filename)
    for i in range(0, len(list_letters_time), 2):
        composing_for_letter = composing_calculate(list_letters_time[i], int(
            list_letters_time[i + 1]))
        for value in composing_for_letter:
            final_composing.append(value)
    pass_menu(final_composing, SAMPLE_RATE)


def pass_menu(audio_data, frame_rate):
    """A function that operates the pass menu which saves a wav file or changes
    one by moving the file to the change menu"""
    action = input(PASS_MENU_MSG)
    if action == "1":
        file_name = input("Enter a file name for the new audio")
        success = save_wave(frame_rate, audio_data, file_name)
        while success == -1:
            file_name = input("Enter a file name for the new audio")
            success = save_wave(frame_rate, audio_data, file_name)
        entrance_menu()
    elif action == "2":
        change_wav_file(audio_data, frame_rate)

def entrance_menu():
    """A function that operates the entrance menu- the user will enter a number
    of action and the function will summon the matching action"""
    action = input(ACTION_MSG)
    if action == "1":
        change_wav_file()
    elif action == "2":
        combine_files_menu()
    elif action == "3":
        composing()
    elif action == "4":
        exit()


if __name__ == '__main__':
    entrance_menu()
