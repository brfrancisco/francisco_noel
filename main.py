import streamlit as st


def parameters_question(person):
    lis_question_fab = [
        ['De combien saison est composée la série : Ici tout commence',
            [1, 2, 3, 4]],
        ['Au basket, sur un rebond offensif, à combien redémarre le chronométre ?',
            [8, 12, 14, 24]],
        ["Quel est l'intitulé du master psychologie clinique de Morgane ?",
                ["thérapies comportementales, cognitives et émotionnelle",
                 'trouble comportementales et cognitives',
                 'thérapies comportementales et cognitives',
                 'trouble comportementales, cognitives et émotionnelle']],
        ["Comment s'appelle les frères de la série Mon Oncle Charlie ?",
                    ["Charlie - Alan", 'Charles - Alain', 'Charles - Alan', 'Charlie - Alain']],
        ["Quel bijou prefere Morgane ?",
                    ["or", 'argent', 'bronze']]
    ]
    right_answer_fab = [2, 14, 'thérapies comportementales, cognitives et émotionnelle', 'Charlie - Alan', 'argent']

    lis_question_paul = [
        ['Combien de ligue des champions ont été remportées par le Barca ?',
            [3, 4, 5, 6]],
        ['Quelle est la date de la bataille de Waterloo ?',
            ["20 Juin 1815", "18 Juin 1816", "20 Juin 1816", "18 Juin 1815"]],
        ["Quel est l'âge de noisette ?",
                [5, 6, 7, 8]],
        ["Comment s'appelle le directeur de la série Ici tout commence ?",
                    ["Emmanuel Teyssier", 'Thomas Teyssier', 'Manuel Teyssier', 'Augustin Galiana']],
        ["Quel aliment n'aime pas Morgane ?",
                    ["chocolat", 'fraise', 'caramel', 'vanille']]
    ]
    right_answer_paul = [5, '18 Juin 1815', 6, 'Emmanuel Teyssier', 'chocolat']

    if person == 'Paul':
        return lis_question_paul, right_answer_paul
    else:
        return lis_question_fab, right_answer_fab


def check_res(right_answers):

    tot_ra = 0
    for i in range(len(st.session_state['rep_question'])):
        r = st.session_state['rep_question'][i]
        if r == right_answers[i]:
            tot_ra += 1

    return tot_ra


def plot_right_answer():
    st.markdown("![Alt Text](https://media.giphy.com/media/9JnU6uRRblKM3hGzu3/giphy.gif)")
    st.markdown("<h2>Bravo tu as bien mérité ton cadeau</h2>", unsafe_allow_html=True)


def plot_bad_answer():
    st.markdown("![Alt Text](https://media.giphy.com/media/ljtfkyTD3PIUZaKWRi/giphy.gif)")
    st.markdown("<h2>Mince tu as echoué</h2>", unsafe_allow_html=True)
    st.markdown("<h2>Ne t'en fais pas, Santa a quand même un cadeau pour toi</h2>", unsafe_allow_html=True)


st.title('Oh Oh Oh')
st.image('pere_noel.jpg')
st.markdown('<h1>Bienvenue à ce test pour vérifier que tu mérites tes cadeaux ! </h1>', unsafe_allow_html=True)
select_person = st.selectbox('Qui es tu', ['Paul', 'Fabienne'])
lis_question, right_answer = parameters_question(select_person)

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
    nb_rep = check_res(right_answer)
    st.markdown(f"<h3>Nombre de réponses juste : {nb_rep} sur 5</h3>", unsafe_allow_html=True)
    if nb_rep >= 3:
        plot_right_answer()
    else:
        plot_bad_answer()

    if st.button('Afficher le cadeau'):
        if select_person == 'Paul':
            st.markdown("![Alt Text](https://media.giphy.com/media/5gzCGDLoZg5jwppe3a/giphy.gif)")
        else:
            st.markdown("![Alt Text](https://media.giphy.com/media/ZG5Si43qz4LLIeu7jF/giphy.gif)")

    if st.button('Recommence'):
        st.session_state['question_number'] = 0
        st.session_state['rep_question'] = []
        st.rerun()


