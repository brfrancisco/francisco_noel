import streamlit as st


st.title('Oh Oh Oh')
st.image('pere_noel.jpg')
st.markdown('<h1>Bienvenue à ce test pour vérifier que tu mérites tes cadeaux ! </h1>', unsafe_allow_html=True)
select_person = st.selectbox('Qui es tu', ['Paul', 'Fabienne'])


lis_question = [
    ['## Quelle année blalbla', [195, 196, 198]],
    ['Super Choix CA' , ['blue', 'red', 'yellow', 'green']]
]

right_answer = [195, 'blue']


def check_res(right_answer):

    tot_ra = 0
    for i in range(len(st.session_state['rep_question'])):
        r = st.session_state['rep_question'][i]
        if r == right_answer[i]:
            tot_ra += 1

    return tot_ra



if 'question_number' not in st.session_state:
    st.session_state['question_number'] = 0
    st.session_state['rep_question'] = []

if st.session_state['question_number']<len(lis_question):
    q = lis_question[st.session_state['question_number']][0]
    p = lis_question[st.session_state['question_number']][1]
    rep = st.radio(q, p)

    if st.button('Validate'):
        st.session_state['question_number'] += 1
        st.session_state['rep_question'].append(rep)
        st.rerun()
else:
    st.write('ON EST AU BOUT')
    nb_rep = check_res(right_answer)
    st.write(nb_rep)
    if st.button('Recommence'):
        st.session_state['question_number'] = 0
        st.session_state['rep_question'] = []
        st.rerun()


