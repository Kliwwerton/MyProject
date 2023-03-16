PRESS_PARAMETERS = {'LAEIS-1250': [1250, 11.98, 'N/см[sup]2[/sup]'],
                    'SACMI-1000': [990, 350, 'Бар'],
                    'SACMI-500': [500, 350, 'Бар'],
                    'YPR-2500': [2500, 28.9, 'kN'],
                    'ДО-542': [1600, 320, 'Атм'],
                    'ДА-2238 (ЦИЧО)': [630, 320, 'Атм'],
                    'СМ-1085': [630, 90, 'Ампер'],
                    'ПЮ': [200, 90, 'Ампер'],
                    'ПД-476 (ЦИЧО)': [160, 320, 'Атм'],
                    'П-483 (ЦИЧО)': [63, 320, 'Атм'],
                    'П-474А (ЦИЧО)': [100, 320, 'Атм'],
                    'ИП-500М-АВТО': [50, 500, 'kN']
                    }

GOST_STANDARDS = {
    'ГОСТ 8691-2018': {'1': [230, 65, 65], '2': [230, 85, 65],
                       '3': [230, 114, 100], '4': [230, 114, 75],
                       '5': [230, 114, 65], '6': [230, 114, 40],
                       '6a': [230, 150, 65], '7': [250, 124, 75],
                       '8': [250, 124, 65], '9': [300, 150, 65],
                       '10': [345, 150, 75], '11': [230, 172, 75],
                       '12': [230, 172, 65], '13': [250, 187, 75],
                       '14': [250, 187, 65], '15': [300, 225, 65],
                       '16': [172, 114, 75], '17': [172, 114, 65],
                       '18': [187, 124, 75], '19': [187, 124, 65],
                       '20': [230, 114, 75, 65], '21': [230, 114, 75, 55],
                       '22': [230, 114, 65, 55], '23': [230, 114, 65, 45],
                       '23a': [230, 150, 75, 45], '24': [250, 124, 75, 65],
                       '25': [250, 124, 65, 55], '26': [250, 124, 65, 45],
                       '27': [172, 114, 65, 55], '28': [172, 114, 65, 45],
                       '29': [300, 150, 65, 55], '30': [300, 150, 65, 45],
                       '31': [345, 150, 75, 65], '32': [345, 150, 75, 55],
                       '33': [230, 172, 75, 65], '34': [230, 172, 75, 55],
                       '35': [230, 172, 65, 55], '36': [230, 172, 65, 45],
                       '37': [250, 187, 75, 65], '38': [250, 187, 65, 55],
                       '39': [250, 187, 65, 45], '40': [300, 225, 65, 55],
                       '41': [300, 225, 65, 45], '42': [230, 114, 75, 65],
                       '43': [230, 114, 75, 55], '44': [230, 114, 65, 55],
                       '45': [230, 114, 65, 45], '45а': [230, 150, 65, 55],
                       '45б': [230, 150, 65, 45], '46': [250, 124, 75, 65],
                       '47': [250, 124, 65, 55], '48': [250, 124, 65, 45],
                       '49': [230, 114, 96, 65], '50': [230, 114, 76, 65],
                       '51': [230, 114, 56, 65], '52': [345, 150, 125, 75],
                       '53': [345, 150, 90, 75], '54': [345, 150, 80, 75],
                       '55': [114, 230, 180, 65], '56': [114, 230, 190, 65],
                       '57': [114, 230, 200, 65], '58': [114, 230, 210, 65],
                       '59': [114, 230, 220, 65],

                       '94': [460, 230, 75], '95': [575, 170, 80],
                       '96': [600, 230, 90], '97': [460, 133, 114],
                       },

    'ГОСТ 1598-2018 (ШПД)': {'1': [230, 150, 75], '2': [345, 150, 75],
                             '3': [230, 115, 75], '4': [345, 115, 75],
                             '5': [230, 150, 150], '6': [345, 150, 150],
                             '7': [230, 150, 90], '8': [230, 150, 109, 62],
                             '9': [230, 150, 135, 75], '10': [345, 150, 125, 75],
                             '11': [230, 150, 120, 75], '12': [345, 150, 110, 75]
                             },

    'ГОСТ 1598-2018 (МЛЛД)': {'1': [550, 200, 150], '2': [550, 200, 120],
                              '3': [400, 200, 120], '4': [400, 200, 100],
                              '5': [550, 200, 150, 75], '6': [550, 200, 100, 50],
                              '7': [400, 200, 120, 75], '8': [400, 200, 120, 50]
                              },

    'ГОСТ 5341-2016': {'1': [250, 140, 65, 120], '2': [250, 140, 80, 125],
                       '2а': [300, 120, 80, 68], '2б': [300, 160, 80, 68],
                       '3': [250, 140, 135, 65], '4': [250, 140, 135, 80],
                       '6': [80, 250, 239, 80], '7': [100, 210, 181, 80],
                       '8': [100, 230, 209, 80], '9': [100, 250, 236, 80],
                       '10': [120, 210, 176, 80], '11': [120, 230, 206, 80],
                       '12': [120, 230, 212, 80], '13': [120, 250, 235, 80],
                       '14': [150, 210, 178, 80], '14a': [150, 225, 205, 80],
                       '15': [150, 230, 205, 80], '15a': [150, 245, 210, 80],
                       '16': [150, 250, 235, 80], '16a': [150, 250, 228, 80],
                       '18': [200, 220, 192, 80], '19': [200, 240, 216, 80],
                       '20': [250, 230, 200, 80], '21': [250, 250, 221, 80],
                       '37': [250, 100, 80], '38': [300, 120, 80], '39': [300, 150, 80]
                       },

    'ГОСТ 5500-2001': {'1-300': [100, 40, 300], '2-300': [125, 48, 300], '3-300': [140, 54, 300],
                       '4-300': [160, 60, 300], '5-300': [180, 64, 300], '6-300': [180, 64, 300],
                       '7-270': [200, 64, 270], '8-270': [200, 64, 270], '8-1-270': [200, 64, 270],
                       },

    'ГОСТ 11586-2005': {'6-250': [120, 70, 250], '6-300': [120, 70, 300], '7-250': [140, 80, 250],
                        '7-300': [140, 80, 300], '8-250': [150, 90, 250], '8-300': [150, 90, 300],
                        '9-190': [160, 100, 190], '9-250': [160, 100, 250], '9-300': [160, 100, 300],
                        '10-250': [180, 100, 250], '10-300': [180, 120, 300]
                        },

    'ГОСТ 21436-2004': {'1': [300, 150, 100, 88], '2': [300, 150, 75, 55], '3': [200, 150, 100, 92],
                        '4': [200, 150, 75, 65], '5': [200, 150, 75, 55], '6': [230, 150, 100, 95],
                        '7': [230, 150, 100, 91], '8': [230, 150, 120, 113], '9': [300, 150, 100, 93],
                        '10': [300, 200, 100, 93], '11': [300, 200, 100, 88], '12': [230, 200, 100, 91],
                        '13': [230, 200, 120, 113], '14': [200, 200, 100, 92], '15': [200, 200, 75, 65],
                        '16': [160, 200, 100, 94], '17': [160, 200, 75, 67], '18': [160, 200, 75, 60],
                        '19': [120, 200, 100, 95], '20': [120, 200, 75, 65], '21': [230, 200, 80, 73],
                        '22': [230, 200, 120, 113], '23': [230, 200, 65, 55], '24': [200, 120, 70, 62],
                        '25': [200, 150, 70, 62], '26': [200, 120, 70, 57], '27': [200, 150, 70, 57],
                        '28': [230, 150, 65, 55], '29': [230, 150, 80, 73], '30': [230, 150, 120, 113],
                        '31': [230, 150, 103, 92], '32': [230, 200, 103, 92], '33': [230, 150, 103, 97],
                        '34': [230, 200, 103, 97], '35': [160, 150, 80, 75], '36': [160, 150, 65, 58],
                        '37': [160, 150, 120, 115], '38': [230, 115, 80, 73], '39': [230, 115, 65, 55]

                        },

    'ГОСТ 20901-2016': {'1': [230, 150, 75], '2': [345, 150, 75], '3': [450, 150, 75],
                        '4': [230, 150, 100], '5': [345, 150, 100], '6': [450, 150, 100],
                        '7': [230, 150, 135, 75], '8': [230, 150, 120, 75], '9': [345, 150, 125, 75],
                        '10': [345, 150, 110, 75], '11': [450, 150, 115, 75], '12': [230, 150, 135, 100],
                        '13': [230, 150, 125, 100], '14': [345, 150, 120, 100], '15': [345, 150, 110, 100],
                        '16': [450, 150, 115, 100], '17': [450, 150, 117, 84, 84, 65, 65],
                        '75': [230, 130, 40], '76': [170, 150, 50], '77': [230, 170, 50],
                        '78': [230, 150, 50]
                        }
}

RECTANGLES = {'ГОСТ 8691-2018': ['1', '2', '3', '4', '5', '6', '6a', '7', '8', '9',
                                 '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                                 '94', '95', '96', '97'],
              'ГОСТ 1598-2018 (ШПД)': ['1', '2', '3', '4', '5', '6', '7'],
              'ГОСТ 1598-2018 (МЛЛД)': ['1', '2', '3', '4'],
              'ГОСТ 5341-2016': ['37', '38', '39'],
              'ГОСТ 20901-2016': ['1', '2', '3', '4', '5', '6', '75', '76', '77', '78'],
              'Прямоугольник': ['Не определён.']
              }

TRAPEZOID = {'Image': 'Images/Product_shape/trapezoid.png',
             'ГОСТ 5341-2016': ['6', '7', '8', '9', '10', '11', '12', '13',
                                '14', '14a', '15', '15a', '16', '16a',
                                '18', '19', '20', '21'],
             'ГОСТ 8691-2018': ['55', '56', '57', '58', '59']
             }

TRAPEZOID_1 = {'Image': 'Images/Product_shape/trapezoid_1.png',
               'Трапецеидальный клин': ['Не определён.'],
               'ГОСТ 1598-2018 (ШПД)': ['9', '10', '11', '12'],
               'ГОСТ 5341-2016': ['3', '4'],
               'ГОСТ 8691-2018': ['49', '50', '51', '52', '53', '54'],
               'ГОСТ 20901-2016': ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
               }

RIBBED = {'Image': 'Images/Product_shape/ribbed.png',
          'Ребровый клин': ['Не определён.'],
          'ГОСТ 1598-2018 (ШПД)': ['8'],
          'ГОСТ 8691-2018': ['42', '43', '44', '45', '45а', '45б', '46', '47', '48'],
          }

RIBBED_1 = {'Image': 'Images/Product_shape/ribbed_1.png',
            'ГОСТ 1598-2018 (МЛЛД)': ['5', '6', '7', '8']
            }

RIBBED_2 = {'Image': 'Images/Product_shape/ribbed_2.png',
            'ГОСТ 5341-2016': ['1', '2', '2а', '2б']
            }

RIBBED_3 = {'Image': 'Images/Product_shape/ribbed_3.png',
            'ГОСТ 21436-2004': ['16', '17', '18', '19', '20']
            }

END_WEDGE = {'Image': 'Images/Product_shape/end_wedge.png',
             'ГОСТ 21436-2004': ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                 '10', '11', '12', '13', '14', '15', '21', '22', '23', '24',
                                 '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
                                 '35', '36', '37', '38', '39']
             }

END_WEDGE_2 = {'Image': 'Images/Product_shape/end_wedge_2.png',
               'ГОСТ 8691-2018': ['20', '21', '22', '23', '23a', '24', '25',
                                  '26', '27', '28',
                                  '29', '30', '31', '32', '33', '34', '35',
                                  '36', '37', '38', '39', '40', '41']
               }

TUBE = {'Image': 'Images/Product_shape/stopor.png',
        'ГОСТ 5500-2001': ['1-300', '2-300', '3-300', '4-300', '5-300', '6-300', '7-270', '8-270', '8-1-270']
        }

TUBE_1 = {'Image': 'Images/Product_shape/center.png',
        'Трубка': ['Не определён.'],
          'ГОСТ 11586-2005': ['6-250', '6-300', '7-250', '7-300', '8-250', '8-300', '9-190', '9-250',
                              '9-300', '10-250', '10-300']
         }

SHAPED = {'Image': 'Images/Product_shape/shaped.png',
          'ГОСТ 20901-2016': ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26']}

VALUES = {}
