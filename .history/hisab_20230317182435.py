import numpy as np
import streamlit as st

import pandas as pd

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    
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
            ' ':0,
            'ـ':0,
            'ّ':0,
            'َ':0,
            'ً':0,}

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

def hisab_sarir(s):
    """Hisab sarir"""
    sum = 0
    for i in s:
        sum += d_abajad[i]
    return sum

# delete extra'ـ' from phrase
def delete_extra(text):
    for i in range(len(text)):
        if text[i] == 'ـ':
            if text[i-1] == 'ـ':
                text = text[:i-1] + text[i:]
    return text

# 
def get_maratib(t):
    l = []
    for c in t:
            n = hisab_sarir(c)
            if n<10:
                n=n
            if 10<=n<100:
                n=n//10
            if n>=100:
                n=n//100
            if n!= 0:
                l.append(n)
    return sum(l)

MOD = True


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

def write_notes(text,title):
    import os
    #chek if data exist
    if  os.path.isfile('notes.csv'):
        # read data
        df = pd.read_csv('notes.csv')
        if title in df['title'].values:
            # update note
            df.loc[df['title']==title,'text'] = text
        else :
            df = df.append({'title':title,'text':text},ignore_index=True)
        # save
        df.to_csv('notes.csv',index=False)
        
    else:
        # create new file
        df = pd.DataFrame({'title':[title],'text':[text]})
        df.to_csv('notes.csv',index=False)

def read_notes():
    import os
    #chek if data exist
    if  os.path.isfile('notes.csv'):
        # read data
        df = pd.read_csv('notes.csv')
        return df
    else:
        return None
    
        
def main():
    st.markdown('<style>body{background-color: #F0F8FF;}</style>',unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 30px; font-weight: bold;">المساعد الحرفي</p>', unsafe_allow_html=True)
    #st.subheader('برمجة : أيوب أبرايش')
    # subheader html center
    st.markdown('<p style="text-align: center; font-size: 20px; font-weight: bold;">برمجة : أيوب أبرايش</p>', unsafe_allow_html=True)
    
    
    
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    with st.expander('Multiple'):
        nn = 
    with st.expander('Notes'):
        title = st.text_input('Title')
        text = st.text_area('Text')
        if st.button('Save'):
            write_notes(text,title)
        df = read_notes()
        
        for title, text in zip(df['title'],df['text']):
            st.markdown(f'<p style="text-align: center; font-size: 20px; font-weight: bold;">{title}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="text-align: right; font-size: 20px; font-weight: bold;">{text}</p>', unsafe_allow_html=True)
            st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    with st.expander('images mojarabat'):
        # show all images in directory, jpg and png
        import os
        images = [f for f in os.listdir('./') if f.endswith('.jpg') or f.endswith('.png')]
        # slide gallery
        for image in images:
            st.image(image, use_column_width=True)
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    # slide 
    with st.expander( 'Quoran'):
        import pandas as pd
        df = pd.read_csv('sura_hisab.csv')
        num = st.number_input('السورة', min_value=1)
        aya = st.number_input('الآية', min_value=1)
        
        def look_num_sura(num):
            return df[df['sura_hisab'] == num]

        def look_num_aya(num):
            return df[df['sura_ayat'] == num]

        st.dataframe(look_num_sura(num))
        st.dataframe(look_num_aya(aya))
        st.write( f'N<{aya}:')
        st.dataframe(df[df['sura_ayat'] < aya])
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)

    
    text_0= """"""
    # center text
    # clear button
    if st.button('مسح'):
        text_0 = ''
    text = st.text_area('ادخل النص هنا', value=text_0, height=200)
    #suggestions
    import pandas as pd
    import os
    if os.path.exists('suggestions.csv'):
        df = pd.read_csv('suggestions.csv')
        sug = df['suggestions'].tolist()
        sug = [s for s in sug if s != '']
        
    else:
        sug = ['منع القرين والعين والسحر و كل اذى روحاني وشيطاني وسحر وتوابع عن ايوب بن جميله']
    
    
    if text != '' and text not in sug:
        sug.append(text)
            
    df = pd.DataFrame(sug,columns=['suggestions'])
        
    
    df.to_csv('suggestions.csv',index=False)
        
    if st.checkbox('اقتراحات'):
        text = st.selectbox('اختر اقتراح',sug)

 
    ## 
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; color: red;">Hisab Kabir = {hisab_sarir(text)}', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; color: red;">Hisab Maratib = {get_maratib(text)}', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; color: red;">Sum Kabir+Maratib = {get_maratib(text)+hisab_sarir(text)}', unsafe_allow_html=True)
    

    #add url = http://holyquran.net/quran/index.html 
    #st.markdown('<p style="text-align: center; font-size: 20px; font-weight: bold;"><a href="http://holyquran.net/quran/index.html">نسخ سور القران</a></p>', unsafe_allow_html=True)
    
    # طلسم المنع
    #if st.checkbox(' طلسم المنع'):
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    #new line in html : <br>
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh;">abjad to abath: <br> {abjad_to_abath(text)}', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh;">abath to abjad: <br> {abath_to_abjad(text)}', unsafe_allow_html=True) 

   
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
      
 
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
   
    with st.expander('Permutation Abajad'):
        N = st.number_input('N',min_value=2,value=2)
        N = int(N)
        text_ = text
        l = []
        for i in range(1,N+1):
            text_permutation = abjad_to_abath(text_)[1]
            l.append(text_permutation)
            text_ = text_permutation
            
        st.write(l)
    
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)


    if st.button( 'اسماء الله الحسنى') :
        n_asma = [(hisab_sarir(k),hisab_sarir(k)-31) for k in l_asma]
        d_as = dict(zip(l_asma,n_asma))
        st.write(d_as)
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)

    count,d_sawa9it = count_horof(text)
    sum_sarir = hisab_sarir(text)
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)

 
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    talsam = sum_sarir * 195555521 
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">طلسم المنع = {talsam}</p>', unsafe_allow_html=True)
    # 
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">طلسم المنع = {convert_number(talsam)}</p>', unsafe_allow_html=True)


    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    talsam = sum_sarir * 469925052834290924265413  
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">طلسم الطلاسم = {talsam}</p>', unsafe_allow_html=True)
    #
    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">طلسم الطلاسم = {convert_number(talsam)}</p>', unsafe_allow_html=True)
    st.info("""ثم ترسم عددك الجديد وتكتب حوله حروفا مفرقة
                    كـ هـ ي ع ص ح م ع س ق أ ن ب أ ت ش ع ر ر أ س ف ل أ ن ب ن ف ل أ ن هـ
                    وتدور بها دائريا حول عددك حتى تغلق به دائريا أو أكثر من دائرة المهم تتم العبارة لو مرتين
                    أو أكثر بحسب ما تغلق عليه دائريا""")
    
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    
    # riz9 
    tal_riz9= sum_sarir * 666221111777

    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">طلسم الرزق = {tal_riz9}</p>', unsafe_allow_html=True)
    # to arabic number

    st.markdown(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; font-weight: bold; font-size: 20px;">طلسم الرزق = {convert_number(tal_riz9)}</p>', unsafe_allow_html=True)
    st.info("""
            تجمع إسمك فلان بن فلانه أو فلانه بنت فلانه بالجمل الكبير

            وتضرب الجمله في عدد الطلسم وهو

            666221111777


            ثم تكتب حوله الحروف مع إسمك مفرقة دائريا كما فعلت أنا بالطلسم

            وهي هذه الحروف

            ز ع ع أ أ ي ق ر ر و س س ثم إسمك ف ل أ ن ب ن ف ل أ ن هـ

            دائريا تقفل بها على الطلسم الجديد ناتج ضربك وتلاحظون أني أعددت الكتابه مرتين حول الطلسم لأجل أقفل عليه دائريا

            """)
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    def get_num(t):
        l = []
        for c in t:
                n = hisab_sarir(c)
                if n<10:
                    n=n
                if 10<=n<100:
                    n=n//10
                if n>=100:
                    n=n//100
                print(f'{c} : {n}')
                if n!= 0:
                    l.append(n)
        print(l)
        return ''.join([str(i) for i in l][::-1])
    t =  st.text_input('النص')
    st.info("""
            1- ﴿ٱللَّهُ لَاۤ إِلَـٰهَ إِلَّا هُوَ ٱلۡحَیُّ ٱلۡقَیُّومُۚ لَا تَأۡخُذُهُۥ سِنَةࣱ وَلَا نَوۡمࣱۚ لَّهُۥ مَا فِی ٱلسَّمَـٰوَ ٰ⁠تِ وَمَا فِی ٱلۡأَرۡضِۗ مَن ذَا ٱلَّذِی یَشۡفَعُ عِندَهُۥۤ إِلَّا بِإِذۡنِهِۦۚ یَعۡلَمُ مَا بَیۡنَ أَیۡدِیهِمۡ وَمَا خَلۡفَهُمۡۖ وَلَا یُحِیطُونَ بِشَیۡءࣲ مِّنۡ عِلۡمِهِۦۤ إِلَّا بِمَا شَاۤءَۚ وَسِعَ كُرۡسِیُّهُ ٱلسَّمَـٰوَ ٰ⁠تِ وَٱلۡأَرۡضَۖ وَلَا یَـُٔودُهُۥ حِفۡظُهُمَاۚ وَهُوَ ٱلۡعَلِیُّ ٱلۡعَظِیمُ﴾ [البقرة ٢٥٥]
            
            2- ﴿ٱللَّهُ لَاۤ إِلَـٰهَ إِلَّا هُوَ ٱلۡحَیُّ ٱلۡقَیُّومُ﴾ [آل عمران ٢]
            
            3 - ﴿ٱللَّهُ لَاۤ إِلَـٰهَ إِلَّا هُوَۚ لَیَجۡمَعَنَّكُمۡ إِلَىٰ یَوۡمِ ٱلۡقِیَـٰمَةِ لَا رَیۡبَ فِیهِۗ وَمَنۡ أَصۡدَقُ مِنَ ٱللَّهِ حَدِیثࣰا﴾ [النساء ٨٧]
            
            4- ﴿ٱللَّهُ لَاۤ إِلَـٰهَ إِلَّا هُوَۖ لَهُ ٱلۡأَسۡمَاۤءُ ٱلۡحُسۡنَىٰ﴾ [طه ٨]
            
            5 - ﴿ٱللَّهُ لَاۤ إِلَـٰهَ إِلَّا هُوَ رَبُّ ٱلۡعَرۡشِ ٱلۡعَظِیمِ ۩﴾ [النمل ٢٦]
            
            6 - ﴿ٱللَّهُ لَاۤ إِلَـٰهَ إِلَّا هُوَۚ وَعَلَى ٱللَّهِ فَلۡیَتَوَكَّلِ ٱلۡمُؤۡمِنُونَ﴾ [التغابن ١٣]
            
            ويافرد افردني بعز ورفعة   وباسمك فاخضع لي ملوكا تجبرت
            اله وجبار جليل وجامع  بجاهك اودعني معان بها انطوت
            شكور فوال القلب شكرا لنعمة  شهيد فاشهدني الحفائق اذ بدت
            ويا ثابت الملك العظيم وثابت  باسمك اسمي في السعادة اثبتت
            بظاء ظهور الاسم اسال ظاهرا فيا ظاهر اظهر لي الامور اذا خفت
            خبير فخبرني مناما ويقظه  بما في اصلاحي وقصدي وماحوت
            سالتك يا خلاق خلق مقاصدي فانت الهي خالق الخلق اجمعت
            زكي تعالى عن صفات حوادث فسبحان ربي شانه قد تعظمت
            """)
    
    def permut(l):
            l = list(l)
            l = [str(c) for c in l if c != ' '][::-1]
            n = len(l)
            
            m = []
            for i in range(n):
                m.append((l[i:] + l[:i])[::-1])
            # to matrix
            m_ = np.zeros((n,n),dtype=str)
            for i in range(n):
                for j in range(n):
                    if i == 0:

                        m_[i][j] = m[0][j]
                        
                    else:
                        m_[i][j] = m[i][::-1][n-j-1]
            #rotate : as in miror
            p = np.rot90(m_,1)

            return p
                
    if st.button('taksir'):
        
        
        
        st.write(permut(t))
        

    
    if st.button('مثلث الغزالي'):
        jomal = hisab_sarir(t)
        st.write(f'جمل : {jomal}')
        x,r = divmod(jomal,15)
        st.write('طلسم عددي')
        #st.write(get_num(t))
        st.write(convert_number(get_num(t)))
        st.write(abjad_to_abath(t)[1])
        
        matrix = np.array([[4*x,9*x+r,2*x],
                           [3*x,5*x,7*x+r],
                           [8*x+r,x,6*x]])
        
        mat_mod_10 = np.zeros((3,3),dtype=int)
        for i in range(3):
            for j in range(3):
                mat_mod_10[i,j] = matrix[i,j]%10
        # apply the function convert_number to each element of the matrix
        matrix = np.vectorize(convert_number)(matrix)
        st.write(matrix)
        st.write(mat_mod_10)
        mat_h = np.zeros((3,3),dtype=str)
        for i in range(3):
            for j in range(3):
                if mat_mod_10[i,j] == 0:
                    mat_h[i,j] = 'ا'
                elif mat_mod_10[i,j] == 1:
                    mat_h[i,j] = 'ا'
                elif mat_mod_10[i,j] == 2:
                    mat_h[i,j] = 'ب'
                elif mat_mod_10[i,j] == 3:
                    mat_h[i,j] = 'ج'
                elif mat_mod_10[i,j] == 4:
                    mat_h[i,j] = 'د'
                elif mat_mod_10[i,j] == 5:
                    mat_h[i,j] = 'ه'
                elif mat_mod_10[i,j] == 6:
                    mat_h[i,j] = 'و'
                elif mat_mod_10[i,j] == 7:
                    mat_h[i,j] = 'ز'
                elif mat_mod_10[i,j] == 8:
                    mat_h[i,j] = 'ح'
                elif mat_mod_10[i,j] == 9:
                    mat_h[i,j] = 'ط'
        st.write(mat_h)

    if st.button('مثلث خالي الوسط'):
        jomal = hisab_sarir(t)
        st.write(f'جمل : {jomal}')
        x,r = divmod(jomal,12)
        st.write('طلسم عددي')
        #st.write(get_num(t))
        st.write(convert_number(get_num(abjad_to_abath(t)[1])))
        st.write(abjad_to_abath(t)[1])
        a = 0 #كن
        matrix = np.array([[3*x,8*x+r,1*x],
                           [7*x+r,0,5*x],
                           [2*x,4*x,6*x+r]])
        
        
        # apply the function convert_number to each element of the matrix
        matrix = np.vectorize(convert_number)(matrix)
        st.write(matrix)
        
    if st.button('مخمس'):
        jomal = hisab_sarir(t)
        st.write(f'جمل : {jomal}')
        x,r = divmod(jomal,65)
        
        st.write('طلسم عددي')
        #st.write(get_num(t))
        st.write(convert_number(get_num(abjad_to_abath(t)[1])))
        st.write(abjad_to_abath(t)[1])
        matrix = np.array([[11*x,18*x,25*x+r,2*x,9*x],
                            [10*x,12*x,19*x,21*x+r,3*x],
                            [4*x,6*x,13*x,20*x,22*x+r],
                            [23*x+r,5*x,7*x,14*x,16*x],
                            [17*x,24*x+r,1*x,8*x,15*x]])
        # apply the function convert_number to each element of the matrix
        col_sum = np.sum(matrix,axis=0)
        row_sum = np.sum(matrix,axis=1)
        diag_sum = np.trace(matrix)
        diag2_sum =  np.trace(np.rot90(matrix))
        st.write(col_sum,row_sum,diag_sum,diag2_sum)
        matrix = np.vectorize(convert_number)(matrix)

        st.write(matrix)
        
        
    if st.button('مربع'):
        jomal = hisab_sarir(t)
        st.write(f'جمل : {jomal}')
        x,r = divmod(jomal,34)
        st.write('طلسم عددي')
        #st.write(get_num(t))
        st.write(convert_number(get_num(t)))

        matrix = np.array([[8*x,11*x,14*x+r,x],
                           [13*x+r,2*x,7*x,12*x],
                           [3*x,16*x+r,9*x,6*x],
                            [10*x,5*x,4*x,15*x+r]])
        matrix_n = matrix.copy()
        # apply the function convert_number to each element of the matrix
        matrix = np.vectorize(convert_number)(matrix)
        st.write(matrix)
        
        mat2 = np.array([[2*x,16*x,13*x+r,3*x],
                         [11*x+r,5*x,8*x,10*x],
                         [7*x,9*x+r,12*x,6*x],
                         [14*x,4*x,1*x,15*x+r]])
        mat2_n = mat2.copy()
        # apply the function convert_number to each element of the matrix
        mat2 = np.vectorize(convert_number)(mat2)
        st.write(mat2)
        
        mat3 = np.array([[7*x,12*x,1*x+r,14*x],
                            [2*x+r,13*x,8*x,11*x],
                            [16*x,3*x+r,10*x,5*x],
                            [9*x,6*x,15*x,4*x+r]])
        mat3_n = mat3.copy()
        # apply the function convert_number to each element of the matrix
        mat3 = np.vectorize(convert_number)(mat3)
        st.write("Magic square in Parshavnath temple")
        st.write(mat3)
        st.write('Complement: n**2+1 - n')
        n= 4
        d = n**2+1
        st.write( d - matrix_n)
        st.write( d - mat2_n)
        st.write( d - mat3_n)
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)

    if st.expander('الكلمات المتعلقة بالعدد'):
        number = st.number_input('العدد',min_value=1)

        # find all the words where sum with  hisab_sarir = number
        words = ['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي']
        value = [hisab_sarir(i) for i in words]
        d = dict(zip(words,value))
        # order the dict by value
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        # find quadruplets with repetition
        l = []  
        for k,v in d.items():
            for k1,v1 in d.items():
                for k2,v2 in d.items():
                    if number-v-v1-v2 in d.values():
                        l.append(k)
        
        reptition = [] 
        res = []
        for i in l:
            for k,v in d.items():
                for k1,v1 in d.items():
                    for k2,v2 in d.items():
                        # dont add duplicate
                        if number-v-v1-v2 == d[i] and set([i,k,k1,k2]) not in reptition:
                            if hisab_sarir(i+k+k1+k2) == number:
                                reptition.append(set([i,k,k1,k2]))
                                res.append(i+k+k1+k2)
        st.write(res)
                            
                             
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    
    t_= st.text_area('النص',key='t_')
    # delete \t \n space
    t_ = t_.replace(' ','').replace('\t','').replace('\n','')
    n= st.number_input('الضلع',min_value=3 )
    if st.button('is9at'):
        t,l,s = is9at(t_)
        st.write(f'is9at : {t}')
        horof = ['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي']
        sawa9it = [i for i in horof if i not in t]
        st.write(f'sawa9it: {sawa9it} = {[hisab_sarir(i) for i in sawa9it]} = {sum([hisab_sarir(i) for i in sawa9it])}= {sum([maratib(hisab_sarir(i)) for i in sawa9it])}')
        st.write(f'hisab  : {l[::-1]}')
        st.write(f'maratib : {[maratib(i) for i in l[::-1]]}')
        st.write(f'sum  kabir  : {s}')
        st.write(f'sum maratib : {sum([maratib(i) for i in l[::-1]])}')
    
    if st.button('carré magique'):
        def m(i,j,n):
            # sum of rows, columns and diagonals and reverse diagonals is n(n^2+1)/2
            a = n * ((i+j+(n-3)/2) % n) + ((i+2*j-2) % n) + 1
            return a
        
        if n % 2 == 0:
            st.write('n must be odd')
        matrix = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = m(j + 1, i + 1, n)
        # permutation : 270°
        matrix = np.rot90(matrix,5)
        
        x,r = divmod(hisab_sarir(t_),n*(n**2+1)/2)
        # finds in matrix index of [n**2 , n**2-1 , n**2-2 , n**2-3, ... , n**2-n+1]
        # matrix of 0, and r where index of [n**2 , n**2-1 , n**2-2 , n**2-3, ... , n**2-n+1]
        mat_0 = matrix.copy()
        mat = np.vectorize(lambda x: r if x in np.arange(n**2,n**2-n,-1) else 0)(mat_0)
        st.write(mat)
        st.write(f'(x,r) = ({x},{r})')
        # multiply the matrix by x; add r to last n elements conseecutivs
        mat2 = matrix*x + mat
        st.write(mat2)
        sum_col = np.sum(mat2,axis=0)
        sum_row = np.sum(mat2,axis=1)
        sum_diag = np.trace(mat2)
        sum_rdiag = np.trace(np.rot90(mat2))
        st.write(f'sum_col : {sum_col}')
        st.write(f'sum_row : {sum_row}')
        st.write(f'sum_diag : {sum_diag}')
        st.write(f'sum_rdiag : {sum_rdiag}')

    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
    if st.button('طالع'):
        jomal = hisab_sarir(t)
        st.write(f'جمل : {jomal}')
        day = jomal%7
        heure = jomal%24
        if day == 0:
            st.write('اليوم : السبت')
        if day == 1:
            st.write('اليوم : الأحد')   
        if day == 2:
            st.write('اليوم : الاثنين')
        if day == 3:
            st.write('اليوم : الثلاثاء')
        if day == 4:
            st.write('اليوم : الأربعاء')
        if day == 5:
            st.write('اليوم : الخميس')
        if day == 6:
            st.write('اليوم : الجمعة')
        st.write(f'الساعة بعد الشروق: {heure}')
        tab3 = (jomal + 52)%4
        if tab3 == 0:
            st.write('طبع مائي')
        if tab3 == 1:
            st.write('طبع ناري')
        if tab3 == 2:
            st.write('طبع هوائي')
        if tab3 == 3:
            st.write('طبع ترابي')
    if st.button('حساب القرين'):
        jomal = hisab_sarir(t)
        jour = (jomal+3)%7
        d= {'Dimanche':1,
                'Lundi':2,
                    'Mardi':3,
                        'Mercredi':4,
                            'Jeudi':5,
                                'Vendredi':6,
                                    'Samedi':0}
        for k,v in d.items():
            if jour == v:
                st.write(f'اليوم : {jour} = {k}')
                
        sa3a = (jomal)%24
        st.write(f'الساعة من الشروق: {sa3a}')
        st.markdown(""" تكون الكتابة والتبخير والحمل في الساعة واليوم .. وتعيد التبخير كل يوم في نفس الساعة بان تخرح الوفق مطوي وتبخير وتتامله ساعة متصلا بقرينك    
        """)
        matrix = np.array([[35,63,76,8,36,49,62,9,22],
                           [10,23,60,64,77,33,37,50,6],
                           [48,7,38,21,61,11,75,34,65],
                           [39,52,2,12,25,56,66,79,29],
                            [80,27,67,53,0,40,26,54,13],
                            [55,14,24,28,68,78,1,41,51],
                            [19,59,15,73,32,69,46,5,42],
                            [3,43,47,57,16,20,30,70,74],
                            [71,72,31,44,45,4,17,18,58] 
        ])
        st.write(matrix*jomal)                       
                    
    st.markdown(f'<hr style="border: 2px solid #000000;">', unsafe_allow_html=True)
        
    
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
        #st.write(pd.DataFrame(list(d_sawa9it.keys()),columns=['الحروف السواقط']).T)
        st.write(f'<p style="text-align: center; font-family: KFGQPC Uthman Taha Naskh; color: red; font-weight: bold;">{list(d_sawa9it.keys())}</p>', unsafe_allow_html=True)
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
    
    

    

def convert_number(text):
    text = str(text)
    arabic_numbers = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
    return ''.join([arabic_numbers[int(i)] if i.isdigit() else i for i in text])


def unify_alias(letter):
    if letter == 'أ':
        return 'ا'
    elif letter == 'آ':
        return 'ا'
    elif letter == 'إ':
        return 'ا'
    elif letter == 'ؤ':
        return 'و'
    elif letter == 'ئ':
        return 'ي'
    elif letter == 'ة':
        return 'ه'
    elif letter == 'ى':
        return 'ي'
    elif letter == 'هـ':
        return 'ه'
    elif letter == 'كـ':
        return 'ك'
    else:
        return letter
    
def is9at(t):
    # delete duplicate characters
    t = ''.join(set(t))
    # get the number of each character
    l = [hisab_sarir(i) for i in t]
    # get the sum of the numbers
    s = sum(l)
    return t,l,s
    
def abjad_to_abath(text):
    text = str(text)
    d = {'أ':'أ', 'ب':'ب', 'ت':'ج', 'ث':'د', 'ج':'هـ', 'ح':'و', 'خ':'ز', 'د':'ح', 'ذ':'ط', 'ر':'ي', 'ز':'كـ', 'س':'ل', 'ش':'م', 'ص':'ن', 'ض':'س', 'ط':'ع', 'ظ':'ف', 'ع':'ص', 'غ':'ق', 'ف':'ر', 'ق':'ش', 'كـ':'ت', 'ل':'ث', 'م':'خ', 'ن':'ذ', 'هـ':'ض', 'و':'ظ', 'ي':'غ'}
    d = {unify_alias(k):v for k,v in d.items()}
    
    converted_text = []
    for letter in text:
        if letter in d:
            converted_text.append(d[letter])
        else:
            converted_text.append(letter)
    
    converted_text = [i for i in converted_text if i != ' ']
    return converted_text, "".join(converted_text)

def abath_to_abjad(text):
    text = str(text)
    d = {'أ':'أ', 'ب':'ب', 'ج':'ت', 'د':'ث', 'هـ':'ج', 'و':'ح', 'ز':'خ', 'ح':'د', 'ط':'ذ', 'ي':'ر', 'كـ':'ز', 'ل':'س', 'م':'ش', 'ن':'ص', 'س':'ض', 'ع':'ط', 'ف':'ظ', 'ص':'ع', 'ق':'غ', 'ر':'ف', 'ش':'ق', 'ت':'كـ', 'ث':'ل', 'خ':'م', 'ذ':'ن', 'ض':'هـ', 'ظ':'و', 'غ':'ي'}
    d = {unify_alias(k):v for k,v in d.items()}

    converted_text = []
    for letter in text:

        if letter in d:
            converted_text.append(d[letter])
        else:
            converted_text.append(letter)
    # delete spaces from list
    converted_text = [i for i in converted_text if i != ' ']
    return converted_text, "".join(converted_text)


def maratib(n):
    if n<10:
        n=n
    if 10<=n<100:
        n=n//10
    if n>=100:
        n=n//100
    return n
#if __name__ == '__main__':
main()