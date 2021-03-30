def month_mapper(month):
    switcher = {
        '01': 'number:1',
        '02': 'number:2',
        '03': 'number:3',
        '04': 'number:4',
        '05': 'number:5',
        '06': 'number:6',
        '07': 'number:7',
        '08': 'number:8',
        '09': 'number:9',
        '10': 'number:10',
        '11': 'number:11',
        '12': 'number:12',
    }
    return switcher.get(month, 'January')