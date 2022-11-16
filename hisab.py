import numpy as np
import streamlit as st

import pandas as pd
# arabic reshaper
import arabic_reshaper
import bidi.algorithm as bidialg

# dont show run bar
st.set_option('deprecation.showRunButton', False)
# background image
back_img_path = "./back.jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url("https://raw.githubusercontent.com/roh-gh/roh-gh.github.io/master/back.jpg")
    }}
    </style>
    """,
    unsafe_allow_html=True
)
    
    
d_abajad = {'ا': 1,
            'ب': 2,
            'ج': 3,
            'د': 4,
            'ه': 5,
            'و': 6,
            'ز': 7,
            'ح': 8,
            'ط': 9,
            'ي': 10,
            'ك': 20,
            'ل': 30,
            'م': 40,
            'ن': 50,
            'س': 60,
            'ع': 70,
            'ف': 80,
            'ص': 90,
            'ق': 100,
            'ر': 200,
            'ش': 300,
            'ت': 400,
            'ث': 500,
            'خ': 600,
            'ذ': 700,
            'ض': 800,
            'ظ': 900,
            'غ': 1000,
            'ء': 0,
            'ئ': 0,
            'ؤ': 0,
            'ة':5,
            'ى':1,
            'آ':1,
            'أ':1,
            'إ':1,
            ' ':0}

d_istinta9 = {'ا': 'الف',
                'ب': 'باء',
                'ج': 'جيم',
                'د': 'دال',
                'ه': 'هاء',
                'و': 'واو',
                'ز': 'زاي',
                'ح': 'حاء',
                'ط': 'طاء',
                'ي': 'ياء',
                'ك': 'كاف',
                'ل': 'لام',
                'م': 'ميم',
                'ن': 'نون',
                'س': 'سين',
                'ع': 'عين',
                'ف': 'فاء',
                'ص': 'صاد',
                'ق': 'قاف',
                'ر': 'راء',
                'ش': 'شين',
                'ت': 'تاء',
                'ث': 'ثاء',
                'خ': 'خاء',
                'ذ': 'ذال',
                'ض': 'ضاد',
                'ظ': 'ظاء',
                'غ': 'غين',
                'ء': 'ء',
                'ئ': 'ئ',
                'ؤ': 'ؤ',
                'ة': 'هاء',
                'ى': 'ياء',
                'آ': 'الف',
                'أ': 'الف',
                'إ': 'الف',
                ' ': ' '}

d_kabir = {'ا': 111, 'ب': 3, 'ج': 53, 'د': 35, 'ه': 6, 'و': 13, 'ز': 18, 'ح': 9, 'ط': 10, 'ي': 11, 'ك': 101, 'ل': 71, 'م': 90, 'ن': 106, 'س': 120, 'ع': 130, 'ف': 81, 'ص': 95, 'ق': 181, 'ر': 201, 'ش': 360, 'ت': 401, 'ث': 501, 'خ': 601, 'ذ': 731, 'ض': 805, 'ظ': 901, 'غ': 1060, 'ء': 0, 'ئ': 0, 'ؤ': 0, 'ة': 6, 'ى': 11, 'آ': 111, 'أ': 111, 'إ': 111, ' ': 0}

d_asma = {'الله': 1,
            'الرحمن': 2,
            'الرحيم': 3,
            'الملك': 4,
            'القدوس': 5,
            'السلام': 6,
            'المؤمن': 7,
            'المهيمن': 8,
            'العزيز': 9,
            'الجبار': 10,
            'المتكبر': 11,
            'الخالق': 12,
            'البارئ': 13,
            'المصور': 14,
            'الغفار': 15,
            'القهار': 16,
            'الوهاب': 17,
            'الرزاق': 18,
            'الفتاح': 19,
            'العليم': 20,
            'القابض': 21,
            'الباسط': 22,
            'الخافض': 23,
            'الرافع': 24,
            'المعز': 25,
            'المذل': 26,
            'السميع': 27,
            'البصير': 28,
            'الحكم': 29,
            'العدل': 30,
            'اللطيف': 31,
            'الخبير': 32,
            'الحليم': 33,
            'العظيم': 34,
            'الغفور': 35,
            'الشكور': 36,
            'العلي': 37,
            'الكبير': 38,
            'الحفيظ': 39,
            'المقيت': 40,
            'الحسيب': 41,
            'الجليل': 42,
            'الكريم': 43,
            'الرقيب': 44,
            'المجيب': 45,
            'الواسع': 46,
            'الحكيم': 47,
            'الودود': 48,
            'المجيد': 49,
            'الباعث': 50,
            'الشهيد': 51,
            'الحق': 52,
            'الوكيل': 53,
            'القوي': 54,
            'المتين': 55,
            'الولي': 56,
            'الحميد': 57,
            'المحصي': 58,
            'المبدئ': 59,
            'المعيد': 60,
            'المحيي': 61,
            'المميت': 62,
            'الحي': 63,
            'القيوم': 64,
            'الواجد': 65,
            'الماجد': 66,
            'الواحد': 67,
            'الصمد': 68,
            'القادر': 69,
            'المقتدر': 70,
            'المقدم': 71,
            'المؤخر': 72,
            'الأول': 73,
            'الآخر': 74,
            'الظاهر': 75,
            'الباطن': 76,
            'الوالي': 77,
            'المتعالي': 78,
            'البر': 79,
            'التواب': 80,
            'المنتقم': 81,
            'العفو': 82,
            'الرؤوف': 83,
            'مالك الملك': 84,
            'ذو الجلال والإكرام': 85,
            'المقسط': 86,
            'الجامع': 87,
            'الغني': 88,
            'المغني': 89,
            'المانع': 90,
            'الضار': 91,
            'النافع': 92,
            'النور': 93,
            'الهادي': 94,
            'البديع': 95,
            'الباقي': 96,
            'الوارث': 97,
            'الرشيد': 98,
            'الصبور ': 99}

l_asma = [ k for k in d_asma.keys() ]



MOD = True
def res(text,mod= MOD):
    if mod:
        return text
    else:
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = bidialg.get_display(reshaped_text)
        return bidi_text
def hisab_sarir(s):
    """Hisab sarir"""
    sum = 0
    for i in s:
        sum += d_abajad[i]
    return sum

def hisab_kabir(s):
    """Hisab kabir"""
    sum = 0
    for i in s:
        sum += hisab_sarir(d_istinta9[i])
    return sum 


#utf-8
d_asma_kabir =  {k:hisab_kabir(k) for k in d_asma.keys()}

d_asma_sarir = {k:hisab_sarir(k) for k in d_asma.keys()}

def search_asma(number):
    occurences = []
    for k,v in d_asma_sarir.items():
        if v == number:
            
            print(f'asma sarir: {k} - sum = {v}')
            occurences.append(k)

    for k,v in d_asma_kabir.items():
        if v == number:
            print(f'asma kabir: {k} - sum = {v}')
            occurences.append(k)
    print(f'occurences: {occurences}, Number of occurences: {len(occurences)}')

def search_asma_v0(number):
    occurences = []
    for k,v in d_asma_sarir.items():
        if v == number:
            occurences.append(k)
    for k,v in d_asma_kabir.items():
        if v == number:
            occurences.append(k)
    return occurences
def magic_square(d,m,h,y):
    raw_1 = [d,m,h,y]
    raw_2 = [y+1,h-1,m-3,d+3]
    raw_3 = [m-2,d+2,y+2,h-2]
    raw_4 = [h+1,y-1,d+1,m-1]
    
    np_matrix = np.array([raw_1,raw_2,raw_3,raw_4])
    
    check1 = np_matrix.sum(axis=0)
    check2 = np_matrix.sum(axis=1)
    check3 = np_matrix.diagonal().sum()
    check4 = np.fliplr(np_matrix).diagonal().sum()
    print(f'check1: {check1}, check2: {check2}, check3: {check3}, check4: {check4}')
    return np_matrix


def search_asma_combinaison(number,kabir=True):
    if kabir:
        l_number = [v  for v in d_asma_kabir.values() ]
    else:
        l_number = [v  for v in d_asma_sarir.values() ]
        
    # matrix : l_number x l_number : sum of each row and column
    np_matrix = np.zeros((len(l_number),len(l_number)))
    
            
    if search_asma_v0(number)==[]:
        print('No occurences, begining combinaison search')
        for i in range(len(l_number)):
            for j in range(len(l_number)):
                 np_matrix[i,j] = l_number[i] + l_number[j]  
        print(np_matrix)
        # search for occurences
        occurences = []
        for i in range(len(l_number)):
            for j in range(i,len(l_number)):
                if np_matrix[i,j] == number:
                    print(f'asma sarir: {res(l_asma[i])} - sum = {l_number[i]}')
                    print(f'asma sarir: {res(l_asma[j])} - sum = {l_number[j]}')
                    print(f'asma sarir: {res(l_asma[i])} + {res(l_asma[j])} - sum = {number}')
                    occurences.append({l_asma[i],l_asma[j]})
                    print('#'*50)
                else:
                    pass
        return occurences
      
        
    else:
        print('occurences found')
        print(search_asma_v0(number))
        return search_asma_v0(number)


def count_horof(text):
    count = {}
    stop_car = [' ','.','،','؟','؛','!','(',')','[',']','{','}','<','>','/','\\','|','*','&','^','%','$','#','@','~','`','+','=','_','-','"',"'",':',';', '\n']
    stop_car += ['ُ', 'ْ', 'ِ','َ','ً','ّ','ٌ', '\xa0','\u06dd','ٍ',',' ]
    alias = {'آ':'ا','أ':'ا','إ':'ا','ؤ':'و','ئ':'ي','ة':'ه','ى':'ي'}
    all_horof = ['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي']
    sawa9it = []
    for c in text:
        if c not in stop_car :
            if c in alias.keys():
                c = alias[c]
            #if c in all_horof:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        else:
            pass   
    #sort
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse=True)}
    print(f'Count of horof: {count}')
    # sum 
    sum_sarir = 0
    for k,v in count.items():
        sum_sarir += v* hisab_sarir(k)
    print(f'Count sum  sarir: {sum_sarir}')

    for c in all_horof:
        if c not in count:
            sawa9it.append(c)
    d_sawa9it = {k: hisab_sarir(k) for k in sawa9it}
    # sort by value
    d_sawa9it = {k: v for k, v in sorted(d_sawa9it.items(), key=lambda item: item[1],reverse=True)}
    print(f'sawa9it: {d_sawa9it}')
    print(f'Sum sarir sawa9it= {sum(d_sawa9it.values())}')
    # len
    print(f'Number of sawa9it: {len(d_sawa9it)}')
    return count,d_sawa9it

def main():
    st.markdown('<style>body{background-color: #F0F8FF;}</style>',unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 30px; font-weight: bold;">المساعد الحرفي</p>', unsafe_allow_html=True)
    #st.subheader('برمجة : أيوب أبرايش')
    # subheader html center
    st.markdown('<p style="text-align: center; font-size: 20px; font-weight: bold;">برمجة : أيوب أبرايش</p>', unsafe_allow_html=True)
    text_0= """
    بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ

    الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ

    الرَّحْمَنِ الرَّحِيمِ

    مَالِكِ يَوْمِ الدِّينِ

    إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ

    اهدِنَا الصِّرَاطَ الْمُسْتَقِيمَ

    صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلاَ الضَّالِّينَ
    """
    # center text
    text = st.text_area('ادخل النص هنا', value=text_0, height=200)
    st.info('يمكنك ادخال اسمك واسم امك او سورة او اي نص باللغة العربية  ')
    #add url = http://holyquran.net/quran/index.html 
    st.markdown('<p style="text-align: center; font-size: 20px; font-weight: bold;"><a href="http://holyquran.net/quran/index.html">نسخ سور القران</a></p>', unsafe_allow_html=True)
    if st.button('اضغط هنا للحساب'):
        count,d_sawa9it = count_horof(text)
        # columns=['الحرف','عدد التكرار']
        st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">الحروف الواردة وتكرارها في النص</p>', unsafe_allow_html=True)
        df_count = pd.DataFrame.from_dict(count, orient='index',columns=['عدد التكرار']).T
        st.dataframe(df_count)
        sum_sarir = 0
        for k,v in count.items():
            sum_sarir += v* hisab_sarir(k)
        sum_kabir = 0
        for k,v in count.items():
            sum_kabir += v* hisab_kabir(k)
        
        # format streamlit : text to right, arabic font, bold
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;">مجموع العدد بالجمل الصغير:  {sum_sarir}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;">مجموع العدد بالجمل الكبير:  {sum_kabir}</p>', unsafe_allow_html=True)
        #html line
        st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">الحروف السواقط وتكرارها في النص</p>', unsafe_allow_html=True) 
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;">الحروف السواقط </p>', unsafe_allow_html=True)
        # no index
        st.write(pd.DataFrame(list(d_sawa9it.keys()),columns=['الحروف السواقط']).T)
        #st.write(f'عدد السواقط: {len(d_sawa9it)}')
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;">عدد السواقط:  {len(d_sawa9it)}</p>', unsafe_allow_html=True)
        #st.write(f'مجوع السواقط بالجمل الصغير: {sum(d_sawa9it.values())}')
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;">مجوع السواقط بالجمل الصغير:  {sum(d_sawa9it.values())}</p>', unsafe_allow_html=True)
        #st.write(f'مجوع السواقط بالجمل الكبير: {sum([hisab_kabir(k) for k in d_sawa9it.keys()])}')
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;">مجوع السواقط بالجمل الكبير:  {sum([hisab_kabir(k) for k in d_sawa9it.keys()])}</p>', unsafe_allow_html=True)

        st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">اسماء الله الحسنى الموافقة</p>', unsafe_allow_html=True)             
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;"> بالجمل الكبير :{search_asma_combinaison(sum_kabir,kabir=True)}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold;"> بالجمل الصغير :{search_asma_combinaison(sum_sarir,kabir=False)}</p>', unsafe_allow_html=True)
        

if __name__ == '__main__':
    main()