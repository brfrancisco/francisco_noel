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
                    ["Charlie - Alan", 'Charles - Alain', 'Charles - Alan', 'Charlie - Alain']]
    ]
    right_answer_fab = [2, 14, 'thérapies comportementales, cognitives et émotionnelle', 'Charlie - Alan']

    lis_question_paul = [
        ['Combien de ligue des champions ont été remportées par le Barca ?',
            [3, 4, 5, 6]],
        ['Quelle est la date de la bataille de Waterloo ?',
            ["20 Juin 1815", "18 Juin 1816", "20 Juin 1816", "18 Juin 1815"]],
        ["En quelle année a commencé la série : Mon Oncle Charlie ?",
                [2002, 2003, 2004, 2005]],
        ["Comment s'appelle le directeur de la série Ici tout commence ?",
                    ["Emmanuel Teyssier", 'Thomas Teyssier', 'Manuel Teyssier', 'Augustin Galiana']]
    ]
    right_answer_paul = [5, 14, '18 Juin 1815', 'Emmanuel Teyssier']

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
    #st.markdown("![Alt Text](https://media.giphy.com/media/9JnU6uRRblKM3hGzu3/giphy.gif)")
    st.markdown("![Alt Text](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif)")
    st.markdown("<h2>Congratulazioni!</h2>", unsafe_allow_html=True)


def plot_bad_answer():
    st.markdown("![Alt Text](https://media.giphy.com/media/ljtfkyTD3PIUZaKWRi/giphy.gif)")
    st.markdown("<h2>Fallito</h2>", unsafe_allow_html=True)
    st.markdown("<h2>Ne t'en fais pas, ta mère a quand même un cadeau pour toi!</h2>", unsafe_allow_html=True)


st.title('Buon Compleanno Chiara!')
st.image('anniv.jpg')
st.markdown('<h1>Bienvenue à ce quizz fais par ta maman pour vérifier que tu mérites ton cadeau ! </h1>',
            unsafe_allow_html=True)
#select_person = st.selectbox('Qui es tu', ['Paul', 'Fabienne'])
#lis_question, right_answer = parameters_question(select_person)
lis_question = [
        ['Quel âge Harry Potter a-t-il quand il se rend à Poudlard pour la première fois ?',
            [10, 11, 12, 13]],
        ['Quelles sont les caractéristiques qui représentent généralement les sorciers faisant partie de Gryffondor 🧙‍♀️?',
            ["Equilibre, loyauté, constance et patience",
             "Courage, force d’esprit et hardiesse",
             "Détermination, ruse et adresse",
             "Sagesse, discernement et curiosité"]],
        ["Quelles sont les prochaines sneakers de Lena ?",
                ["Nike vaporwaffle sacai sail gum",
                 "Travis Scott Baskets Air Jordan 1 low OG Reverse Mocha",
                 "Nike Vaporwaffle sacai black white",
                 "Air Jordan 1 low Travis Scott Fragment"]],
        ["Quel est le slogan de la Maison HERMES ?",
                    ["L’esprit d’engagement",
                     'L’esprit de séduction',
                     'L’esprit d’équité',
                     'L’esprit d’entreprendre']],
    ["Quelle est l’heure exacte de ta naissance ?",
        ["10 janvier 1998 à 15H56",
         "10 janvier 1998 à 16H08",
         "10 janvier 1998 à 16H10",
         "10 janvier 1998 à 16H26"]]
    ]
right_answer = [11,
                     "Courage, force d’esprit et hardiesse",
                     'Nike Vaporwaffle sacai black white',
                     "L’esprit d’entreprendre",
                     "10 janvier 1998 à 16H08"]

if 'question_number' not in st.session_state:
    st.session_state['question_number'] = 0
    st.session_state['rep_question'] = []

if st.session_state['question_number']<len(lis_question):
    if st.session_state['question_number'] <= 1:
        st.markdown('### TU TE DIS INCOLLABLE SUR LA SAGA HARRY POTTER 🧙‍♂️ … ')
        st.image('harry.jpg')
    elif st.session_state['question_number'] == 2:
        st.markdown('### Voyons si tu connais les goûts de ta sœur 👟')
    elif st.session_state['question_number'] == 3:
        st.markdown('### En rapport avec tes études 👩‍🎓:')
    elif st.session_state['question_number'] == 4:
        st.markdown('### Et enfin :')
    q = "#### "+lis_question[st.session_state['question_number']][0]
    p = lis_question[st.session_state['question_number']][1]
    rep = st.radio(q, p)

    if st.button('Validate'):
        st.session_state['question_number'] += 1
        st.session_state['rep_question'].append(rep)
        st.rerun()
else:
    nb_rep = check_res(right_answer)
    st.markdown(f"<h3>Nombre de réponses juste : {nb_rep} sur {len(lis_question)}</h3>", unsafe_allow_html=True)
    if nb_rep >= 3:
        plot_right_answer()
    else:
        plot_bad_answer()

    if st.button('Clic ici pour voir ton cadeau'):
        # if select_person == 'Paul':
        #     st.markdown("![Alt Text](https://media.giphy.com/media/5gzCGDLoZg5jwppe3a/giphy.gif)")
        # else:
        #     st.markdown("![Alt Text](https://media.giphy.com/media/jxOx37spvI9h94pnly/giphy.gif)")
        st.markdown("![Alt Text](https://media.giphy.com/media/hTIaAU2vIQyrVQrxGG/giphy.gif)")
        st.image("bag.png")

    if st.button('Recommence'):
        st.session_state['question_number'] = 0
        st.session_state['rep_question'] = []
        st.rerun()


