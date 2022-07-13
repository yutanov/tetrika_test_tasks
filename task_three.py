def appearance(intervals):
    '''
    Получение временных интервалов
    Объединение временных интервалов ученика, в случае их пересечения
    Объединение временных интервалов учителя, в случае их пересечения
    Вычисление общего времени присутствия на уроке учителя и ученика
    '''
    lesson = intervals.get('lesson')
    pupil = union(intervals.get('pupil'))
    tutor = union(intervals.get('tutor'))
    res = 0
    for i in range(0, len(pupil), 2):
        for j in range(0, len(tutor), 2):
            if pupil[i] < tutor[j + 1] and pupil[i + 1] > tutor[j]:
                start = max(pupil[i], tutor[j])
                end = min(pupil[i + 1], tutor[j + 1])
                if start < lesson[1] and end > lesson[0]:
                    res += min(end, lesson[1]) - max(start, lesson[0])
    return res


def union(arr):
    '''
    Нахождение пересекающихся временных интервалов
    Возврат объединенных временных интервалов
    '''
    data = arr.copy()
    res = []
    if len(data) > 0:
        while len(data) != 2:
            if data[1] > data[2]:
                if data[1] > data[3]:
                    data.pop(2)
                    data.pop(2)
                else:
                    data.pop(1)
                    data.pop(1)
            else:
                res.append(data.pop(0))
                res.append(data.pop(0))
        res.append(data.pop(0))
        res.append(data.pop(0))
    return res


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
