# poe: name=Mad-English

import random
import json

class MadEnglish:
    def run(self):
        # Generate 10 random English questions across different categories
        categories = ['grammar', 'vocabulary', 'literature', 'spelling', 'idioms', 'writing']
        difficulty_levels = ['beginner', 'intermediate', 'advanced', 'mastery']

        # Parse user input for category and difficulty preference
        query_text = poe.query.text.lower() if poe.query.text else ""

        # Determine category
        selected_category = 'mixed'
        for cat in categories:
            if cat in query_text:
                selected_category = cat
                break

        # Determine difficulty
        selected_difficulty = 'intermediate'
        if 'beginner' in query_text or 'easy' in query_text or 'basic' in query_text:
            selected_difficulty = 'beginner'
        elif 'advanced' in query_text or 'hard' in query_text or 'difficult' in query_text:
            selected_difficulty = 'advanced'
        elif 'mastery' in query_text or 'master' in query_text or 'expert' in query_text or 'shakespeare' in query_text:
            selected_difficulty = 'mastery'
        elif 'intermediate' in query_text or 'medium' in query_text:
            selected_difficulty = 'intermediate'

        # Generate 10 random questions
        questions = []
        if selected_category == 'mixed':
            # Mix of all categories
            for _ in range(10):
                cat = random.choice(categories)
                questions.append(self.generate_question(cat, selected_difficulty))
        else:
            # Single category
            for _ in range(10):
                questions.append(self.generate_question(selected_category, selected_difficulty))

        # Create the HTML quiz
        html = self.create_quiz_html(questions, selected_category, selected_difficulty)

        # Output the HTML
        with poe.start_message() as msg:
            msg.write(f"````html\n{html}\n````")

    def generate_question(self, category, difficulty):
        """Generate a random question based on category and difficulty"""
        generators = {
            'grammar': self.generate_grammar_question,
            'vocabulary': self.generate_vocabulary_question,
            'literature': self.generate_literature_question,
            'spelling': self.generate_spelling_question,
            'idioms': self.generate_idioms_question,
            'writing': self.generate_writing_question
        }

        return generators[category](difficulty)

    def generate_grammar_question(self, difficulty):
        """Generate random grammar questions"""
        if difficulty == 'beginner':
            templates = [
                {
                    'type': 'parts_of_speech',
                    'words': [
                        ('book', 'noun'), ('run', 'verb'), ('happy', 'adjective'), ('quickly', 'adverb'),
                        ('car', 'noun'), ('jump', 'verb'), ('beautiful', 'adjective'), ('slowly', 'adverb'),
                        ('dog', 'noun'), ('sing', 'verb'), ('tall', 'adjective'), ('loudly', 'adverb')
                    ]
                },
                {
                    'type': 'plural',
                    'words': [
                        ('child', 'children'), ('mouse', 'mice'), ('foot', 'feet'), ('tooth', 'teeth'),
                        ('person', 'people'), ('ox', 'oxen'), ('goose', 'geese'), ('man', 'men')
                    ]
                },
                {
                    'type': 'past_tense',
                    'words': [
                        ('eat', 'ate'), ('run', 'ran'), ('go', 'went'), ('see', 'saw'),
                        ('take', 'took'), ('make', 'made'), ('have', 'had'), ('do', 'did')
                    ]
                }
            ]

            template = random.choice(templates)

            if template['type'] == 'parts_of_speech':
                word, pos = random.choice(template['words'])
                wrong_options = ['noun', 'verb', 'adjective', 'adverb']
                wrong_options.remove(pos)
                options = [pos] + random.sample(wrong_options, 3)
                random.shuffle(options)
                return {
                    'q': f"What part of speech is '{word}'?",
                    'options': options,
                    'answer': options.index(pos)
                }
            elif template['type'] == 'plural':
                singular, plural = random.choice(template['words'])
                wrong = [w[1] for w in template['words'] if w != (singular, plural)]
                options = [plural] + random.sample(wrong, 3)
                random.shuffle(options)
                return {
                    'q': f"What is the plural of '{singular}'?",
                    'options': options,
                    'answer': options.index(plural)
                }
            else:  # past_tense
                present, past = random.choice(template['words'])
                wrong = [w[1] for w in template['words'] if w != (present, past)]
                options = [past] + random.sample(wrong, 3)
                random.shuffle(options)
                return {
                    'q': f"What is the past tense of '{present}'?",
                    'options': options,
                    'answer': options.index(past)
                }

        elif difficulty == 'intermediate':
            question_types = [
                {
                    'q': 'What is the correct form of subject-verb agreement?',
                    'correct': 'The team is playing',
                    'wrong': ['The team are playing', 'The team be playing', 'The teams is playing']
                },
                {
                    'q': 'Identify the conjunction in: "I like tea and coffee"',
                    'correct': 'and',
                    'wrong': ['like', 'tea', 'coffee']
                },
                {
                    'q': 'What is a gerund?',
                    'correct': 'A verb form ending in -ing used as a noun',
                    'wrong': ['Past tense verb', 'An adjective', 'A pronoun']
                },
                {
                    'q': 'Which sentence uses correct parallel structure?',
                    'correct': 'She likes reading, writing, and painting',
                    'wrong': ['She likes reading, writing, and to paint', 'She likes to read, writing, and paint', 'She likes read, write, painting']
                }
            ]

            q_data = random.choice(question_types)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

        elif difficulty == 'advanced':
            question_types = [
                {
                    'q': 'What is a dangling participle?',
                    'correct': 'A participle phrase that doesn\'t logically modify any word',
                    'wrong': ['A verb modifier', 'An incorrect tense', 'A type of noun']
                },
                {
                    'q': 'Identify the subjunctive mood:',
                    'correct': 'If I were rich',
                    'wrong': ['If I was rich', 'If I am rich', 'If I be rich']
                },
                {
                    'q': 'Which demonstrates correct use of "whom"?',
                    'correct': 'To whom did you speak?',
                    'wrong': ['Whom is calling?', 'Whom called you?', 'Whom is that?']
                }
            ]

            q_data = random.choice(question_types)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

        else:  # mastery
            question_types = [
                {
                    'q': 'What is tmesis in linguistics?',
                    'correct': 'Splitting a word with another word (e.g., "abso-bloody-lutely")',
                    'wrong': ['Omitting letters', 'Adding prefixes', 'Combining compound words']
                },
                {
                    'q': 'What is zeugma?',
                    'correct': 'A word applying to two others in different senses',
                    'wrong': ['A palindrome structure', 'A compound word formation', 'A verb conjugation form']
                },
                {
                    'q': 'What is synesis (notional agreement)?',
                    'correct': 'Agreement based on meaning rather than grammatical form',
                    'wrong': ['Strict grammatical agreement', 'Collective noun error', 'Subject-verb disagreement']
                }
            ]

            q_data = random.choice(question_types)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

    def generate_vocabulary_question(self, difficulty):
        """Generate random vocabulary questions"""
        if difficulty == 'beginner':
            word_pairs = [
                ('happy', 'joyful', ['sad', 'angry', 'tired']),
                ('big', 'large', ['small', 'tiny', 'little']),
                ('fast', 'quick', ['slow', 'lazy', 'heavy']),
                ('smart', 'intelligent', ['dumb', 'stupid', 'foolish']),
                ('beautiful', 'pretty', ['ugly', 'plain', 'bad']),
            ]

            word, synonym, antonyms = random.choice(word_pairs)
            question_type = random.choice(['synonym', 'antonym'])

            if question_type == 'synonym':
                options = [synonym] + random.sample(antonyms, 3)
                random.shuffle(options)
                return {
                    'q': f"What is a synonym for '{word}'?",
                    'options': options,
                    'answer': options.index(synonym)
                }
            else:
                options = antonyms + [synonym]
                random.shuffle(options)
                correct = random.choice(antonyms)
                return {
                    'q': f"What is an antonym for '{word}'?",
                    'options': options,
                    'answer': options.index(correct)
                }

        elif difficulty == 'intermediate':
            words = [
                ('benevolent', 'kind and generous', ['evil', 'neutral', 'angry']),
                ('eloquent', 'articulate and persuasive', ['silent', 'confused', 'shy']),
                ('meticulous', 'very careful and precise', ['careless', 'lazy', 'quick']),
                ('tenacious', 'persistent and determined', ['weak', 'giving up easily', 'lazy']),
                ('pragmatic', 'practical and realistic', ['idealistic', 'theoretical', 'emotional']),
            ]

            word, meaning, wrong = random.choice(words)
            options = [meaning] + wrong
            random.shuffle(options)
            return {
                'q': f"What does '{word}' mean?",
                'options': options,
                'answer': options.index(meaning)
            }

        elif difficulty == 'advanced':
            words = [
                ('obsequious', 'excessively compliant or submissive', ['rebellious', 'independent', 'confident']),
                ('perspicacious', 'having keen insight', ['dull', 'ignorant', 'confused']),
                ('quixotic', 'idealistic and impractical', ['practical', 'realistic', 'cynical']),
                ('sanguine', 'optimistic and confident', ['pessimistic', 'neutral', 'depressed']),
                ('recalcitrant', 'stubbornly resistant', ['obedient', 'flexible', 'agreeable']),
            ]

            word, meaning, wrong = random.choice(words)
            options = [meaning] + wrong
            random.shuffle(options)
            return {
                'q': f"What does '{word}' mean?",
                'options': options,
                'answer': options.index(meaning)
            }

        else:  # mastery
            words = [
                ('sesquipedalian', 'characterized by using long words', ['brief', 'simple', 'common']),
                ('grandiloquent', 'pompous or bombastic in language', ['simple speech', 'quiet', 'concise']),
                ('eleemosynary', 'relating to charity or alms', ['selfish', 'greedy', 'commercial']),
                ('anfractuous', 'winding and intricate', ['straight', 'simple', 'direct']),
                ('prelapsarian', 'before the fall from innocence', ['after the fall', 'modern', 'current']),
            ]

            word, meaning, wrong = random.choice(words)
            options = [meaning] + wrong
            random.shuffle(options)
            return {
                'q': f"What does '{word}' mean?",
                'options': options,
                'answer': options.index(meaning)
            }

    def generate_literature_question(self, difficulty):
        """Generate random literature questions"""
        if difficulty == 'beginner':
            questions = [
                {
                    'q': 'Who wrote "Romeo and Juliet"?',
                    'correct': 'William Shakespeare',
                    'wrong': ['Charles Dickens', 'Jane Austen', 'Mark Twain']
                },
                {
                    'q': 'What is a haiku?',
                    'correct': 'A short Japanese poem with 3 lines',
                    'wrong': ['A novel', 'A play', 'A long essay']
                },
                {
                    'q': 'What is the main character in a story called?',
                    'correct': 'Protagonist',
                    'wrong': ['Antagonist', 'Narrator', 'Author']
                },
                {
                    'q': 'What is a metaphor?',
                    'correct': 'A direct comparison between two things',
                    'wrong': ['A comparison using "like" or "as"', 'A sound device', 'A rhyme scheme']
                },
            ]

            q_data = random.choice(questions)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

        elif difficulty == 'intermediate':
            questions = [
                {
                    'q': 'Who wrote "1984"?',
                    'correct': 'George Orwell',
                    'wrong': ['Aldous Huxley', 'Ray Bradbury', 'Kurt Vonnegut']
                },
                {
                    'q': 'What is personification?',
                    'correct': 'Giving human characteristics to non-human things',
                    'wrong': ['A character description', 'A plot device', 'A setting description']
                },
                {
                    'q': 'Who wrote "The Great Gatsby"?',
                    'correct': 'F. Scott Fitzgerald',
                    'wrong': ['Ernest Hemingway', 'John Steinbeck', 'William Faulkner']
                },
            ]

            q_data = random.choice(questions)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

        elif difficulty == 'advanced':
            questions = [
                {
                    'q': 'What is a bildungsroman?',
                    'correct': 'A coming-of-age story',
                    'wrong': ['A war novel', 'A romance', 'A mystery']
                },
                {
                    'q': 'What is stream of consciousness?',
                    'correct': 'Narrative depicting unfiltered thoughts and feelings',
                    'wrong': ['Linear narrative', 'Dialogue-only text', 'Pure description']
                },
                {
                    'q': 'What is metafiction?',
                    'correct': 'Fiction that self-consciously addresses fiction itself',
                    'wrong': ['Science fiction', 'Historical fiction', 'Fantasy']
                },
            ]

            q_data = random.choice(questions)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

        else:  # mastery
            questions = [
                {
                    'q': 'What is "defamiliarization" (ostranenie) in Russian Formalism?',
                    'correct': 'Making the familiar strange to renew perception',
                    'wrong': ['Simplifying complex ideas', 'Character development technique', 'Plot structure method']
                },
                {
                    'q': 'What is "negative capability" according to Keats?',
                    'correct': 'Being in uncertainties without seeking facts',
                    'wrong': ['Critical thinking ability', 'Writer\'s block', 'Pessimistic worldview']
                },
                {
                    'q': 'In Dante\'s "Divine Comedy", what poetic form is used?',
                    'correct': 'Terza rima',
                    'wrong': ['Blank verse', 'Heroic couplets', 'Free verse']
                },
            ]

            q_data = random.choice(questions)
            options = [q_data['correct']] + q_data['wrong']
            random.shuffle(options)
            return {
                'q': q_data['q'],
                'options': options,
                'answer': options.index(q_data['correct'])
            }

    def generate_spelling_question(self, difficulty):
        """Generate random spelling questions"""
        if difficulty == 'beginner':
            words = [
                ('receive', ['recieve', 'recive', 'receeve']),
                ('separate', ['seperate', 'separete', 'seperete']),
                ('definitely', ['definately', 'definatly', 'definetly']),
                ('necessary', ['necesary', 'neccesary', 'neccessary']),
                ('believe', ['beleive', 'beleave', 'belive']),
            ]
        elif difficulty == 'intermediate':
            words = [
                ('embarrass', ['embarass', 'embarras', 'embaress']),
                ('millennium', ['millenium', 'milennium', 'milenium']),
                ('persistent', ['persistant', 'persisttant', 'persistenet']),
                ('questionnaire', ['questionaire', 'questionairre', 'questionnare']),
                ('liaison', ['liason', 'liasion', 'liaision']),
            ]
        elif difficulty == 'advanced':
            words = [
                ('desiccate', ['dessicate', 'desicate', 'dessicatte']),
                ('supersede', ['supercede', 'superceed', 'superseed']),
                ('pharaoh', ['pharoah', 'pharoh', 'pharouh']),
                ('minuscule', ['miniscule', 'minescule', 'miniscul']),
                ('consensus', ['concensus', 'consencus', 'concensuss']),
            ]
        else:  # mastery
            words = [
                ('fuchsia', ['fuschia', 'fushia', 'fuschsia']),
                ('onomatopoeia', ['onomatopeia', 'onomatopoea', 'onomatapoeia']),
                ('sacrilegious', ['sacreligious', 'sacriligious', 'sacrelegious']),
                ('vicissitude', ['vissicitude', 'vicisitude', 'vissisitude']),
                ('palette', ['pallete', 'palet', 'pallette']),
            ]

        correct, wrong_options = random.choice(words)
        options = [correct] + wrong_options
        random.shuffle(options)
        return {
            'q': 'Which is spelled correctly?',
            'options': options,
            'answer': options.index(correct)
        }

    def generate_idioms_question(self, difficulty):
        """Generate random idioms questions"""
        if difficulty == 'beginner':
            idioms = [
                ('break the ice', 'start a conversation', ['destroy ice', 'go skating', 'cool down']),
                ('piece of cake', 'easy task', ['dessert', 'birthday celebration', 'difficult task']),
                ('hit the books', 'study hard', ['hit books physically', 'go to library', 'write books']),
                ('under the weather', 'feeling ill', ['outside', 'happy', 'energetic']),
            ]
        elif difficulty == 'intermediate':
            idioms = [
                ('beat around the bush', 'avoid the main topic', ['garden work', 'be direct', 'fight']),
                ('bite the bullet', 'face difficulty bravely', ['eat something', 'avoid problems', 'celebrate']),
                ('cut to the chase', 'get to the point', ['run away', 'stop talking', 'start slowly']),
                ('spill the beans', 'reveal a secret', ['make a mess', 'keep quiet', 'cook food']),
            ]
        elif difficulty == 'advanced':
            idioms = [
                ('burn bridges', 'destroy relationships', ['commit arson', 'build connections', 'travel across']),
                ('go the extra mile', 'make a special effort', ['travel far', 'give up', 'run fast']),
                ('read between the lines', 'understand hidden meaning', ['poor vision', 'read carefully', 'skip text']),
                ('throw caution to the wind', 'take a risk', ['be very careful', 'weather forecast', 'give up']),
            ]
        else:  # mastery
            idioms = [
                ('gild the lily', 'add unnecessary embellishment', ['garden work', 'improve something', 'destroy beauty']),
                ('hoist by one\'s own petard', 'harmed by one\'s own plan', ['achieve victory', 'succeed greatly', 'celebrate']),
                ('tilting at windmills', 'fighting imaginary enemies', ['jousting sport', 'practical action', 'engineering work']),
                ('to curry favor', 'seek advantage through flattery', ['cook food', 'be honest', 'avoid people']),
            ]

        idiom, meaning, wrong = random.choice(idioms)
        options = [meaning] + wrong
        random.shuffle(options)
        return {
            'q': f"What does '{idiom}' mean?",
            'options': options,
            'answer': options.index(meaning)
        }

    def generate_writing_question(self, difficulty):
        """Generate random writing questions"""
        if difficulty == 'beginner':
            questions = [
                {
                    'q': 'What is a paragraph?',
                    'correct': 'A group of related sentences',
                    'wrong': ['One sentence', 'A title', 'A single word']
                },
                {
                    'q': 'What are the three main parts of an essay?',
                    'correct': 'Introduction, body, conclusion',
                    'wrong': ['Title, body, end', 'Start, middle, stop', 'Beginning, center, finish']
                },
                {
                    'q': 'What is the purpose of a thesis statement?',
                    'correct': 'State the main argument',
                    'wrong': ['End an essay', 'Tell a story', 'Ask questions']
                },
            ]
        elif difficulty == 'intermediate':
            questions = [
                {
                    'q': 'What is a hook in writing?',
                    'correct': 'An opening that grabs attention',
                    'wrong': ['A fishing tool', 'The conclusion', 'A middle paragraph']
                },
                {
                    'q': 'What is tone in writing?',
                    'correct': 'The author\'s attitude toward the subject',
                    'wrong': ['Sound level', 'Volume', 'Reading speed']
                },
                {
                    'q': 'What is plagiarism?',
                    'correct': 'Using others\' work without credit',
                    'wrong': ['Original work', 'Proper citation', 'Research method']
                },
            ]
        elif difficulty == 'advanced':
            questions = [
                {
                    'q': 'What is ethos in rhetoric?',
                    'correct': 'Appeal to credibility and character',
                    'wrong': ['Emotional appeal', 'Logical reasoning', 'Timing']
                },
                {
                    'q': 'What is pathos in rhetoric?',
                    'correct': 'Appeal to emotion',
                    'wrong': ['Logical argument', 'Credibility', 'Evidence-based']
                },
                {
                    'q': 'What is logos in rhetoric?',
                    'correct': 'Appeal to logic and reason',
                    'wrong': ['Emotional appeal', 'Character appeal', 'Style']
                },
            ]
        else:  # mastery
            questions = [
                {
                    'q': 'What is chiasmus?',
                    'correct': 'Reversal of grammatical structures (e.g., "Ask not what...")',
                    'wrong': ['Repetition of words', 'Rhyme scheme', 'Meter pattern']
                },
                {
                    'q': 'What is anadiplosis?',
                    'correct': 'Ending word becomes next sentence beginning',
                    'wrong': ['Beginning repetition', 'Random word placement', 'Parallel structure']
                },
                {
                    'q': 'What is polysyndeton?',
                    'correct': 'Use of multiple conjunctions in close succession',
                    'wrong': ['Omission of conjunctions', 'One conjunction only', 'Complex vocabulary']
                },
            ]

        q_data = random.choice(questions)
        options = [q_data['correct']] + q_data['wrong']
        random.shuffle(options)
        return {
            'q': q_data['q'],
            'options': options,
            'answer': options.index(q_data['correct'])
        }

    def create_quiz_html(self, questions, category, difficulty):
        """Create the HTML quiz interface"""
        questions_json = json.dumps(questions)

        category_icons = {
            'grammar': '📝',
            'vocabulary': '📖',
            'literature': '📕',
            'spelling': '✍️',
            'idioms': '💬',
            'writing': '🖋️',
            'mixed': '🎭'
        }

        difficulty_labels = {
            'beginner': '🟢 Beginner',
            'intermediate': '🟡 Intermediate',
            'advanced': '🔴 Advanced',
            'mastery': '👑 LITERARY MASTERY'
        }

        category_display = category_icons.get(category, '🎭') + ' ' + category.capitalize()
        difficulty_display = difficulty_labels.get(difficulty, '🟡 Intermediate')

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mad English - Dynamic Quiz</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Crimson+Pro:wght@400;600&family=Libre+Baskerville:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Crimson Pro', serif;
            background: linear-gradient(135deg, #2a1a4a 0%, #4a2a5a 50%, #3a1a3a 100%);
            min-height: 100vh;
            color: #2c1810;
            overflow-x: hidden;
            position: relative;
            padding: 20px;
        }}

        .floating-symbols {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }}

        .symbol {{
            position: absolute;
            font-size: 24px;
            opacity: 0.1;
            animation: float 20s infinite;
            color: #ffd700;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0) rotate(0deg); }}
            50% {{ transform: translateY(-100vh) rotate(360deg); }}
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 40px 20px;
            background: linear-gradient(135deg, #f4e9d7 0%, #e8d5b7 100%);
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3), inset 0 0 0 3px #d4af37;
            position: relative;
            overflow: hidden;
        }}

        .header::before {{
            content: '"';
            position: absolute;
            top: -20px;
            left: 20px;
            font-size: 120px;
            color: #d4af37;
            opacity: 0.2;
            font-family: 'Playfair Display', serif;
        }}

        .header::after {{
            content: '"';
            position: absolute;
            bottom: -60px;
            right: 20px;
            font-size: 120px;
            color: #d4af37;
            opacity: 0.2;
            font-family: 'Playfair Display', serif;
        }}

        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 3em;
            font-weight: 900;
            background: linear-gradient(135deg, #6b1f5c 0%, #8b2f6c 50%, #4a0f3c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
        }}

        .subtitle {{
            font-family: 'Libre Baskerville', serif;
            font-size: 1.2em;
            color: #8b4513;
            font-style: italic;
        }}

        .quiz-container {{
            background: linear-gradient(135deg, #f4e9d7 0%, #e8d5b7 100%);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3), inset 0 0 0 3px #d4af37;
        }}

        .quiz-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }}

        .quiz-info {{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .info-badge {{
            background: linear-gradient(135deg, #6b1f5c 0%, #8b2f6c 100%);
            color: #fff;
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: 600;
            border: 2px solid #d4af37;
        }}

        .timer {{
            font-size: 1.3em;
            font-weight: 700;
            color: #6b1f5c;
            font-family: 'Playfair Display', serif;
        }}

        .question-container {{
            margin-bottom: 30px;
        }}

        .question-number {{
            font-family: 'Playfair Display', serif;
            font-size: 1.2em;
            color: #8b4513;
            margin-bottom: 15px;
        }}

        .question-text {{
            font-family: 'Libre Baskerville', serif;
            font-size: 1.4em;
            color: #2c1810;
            margin-bottom: 30px;
            line-height: 1.6;
            padding: 20px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            border-left: 5px solid #6b1f5c;
        }}

        .options {{
            display: grid;
            gap: 15px;
        }}

        .option {{
            background: linear-gradient(135deg, #fff 0%, #f9f9f9 100%);
            border: 3px solid #8b4513;
            padding: 20px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Crimson Pro', serif;
            font-size: 1.1em;
        }}

        .option:hover {{
            transform: translateX(10px);
            border-color: #d4af37;
            box-shadow: 0 5px 20px rgba(212, 175, 55, 0.4);
        }}

        .option.selected {{
            background: linear-gradient(135deg, #6b1f5c 0%, #8b2f6c 100%);
            color: #fff;
            border-color: #d4af37;
        }}

        .option.correct {{
            background: linear-gradient(135deg, #28a745 0%, #20843a 100%);
            color: #fff;
            border-color: #d4af37;
        }}

        .option.incorrect {{
            background: linear-gradient(135deg, #dc3545 0%, #bd2130 100%);
            color: #fff;
            border-color: #d4af37;
        }}

        .next-btn {{
            background: linear-gradient(135deg, #6b1f5c 0%, #8b2f6c 100%);
            color: #fff;
            border: 3px solid #d4af37;
            padding: 15px 40px;
            border-radius: 12px;
            font-family: 'Crimson Pro', serif;
            font-size: 1.2em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            float: right;
            margin-top: 20px;
        }}

        .next-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.8);
        }}

        .hidden {{
            display: none;
        }}

        .results {{
            text-align: center;
        }}

        .results h2 {{
            font-family: 'Playfair Display', serif;
            font-size: 2.5em;
            color: #6b1f5c;
            margin-bottom: 20px;
        }}

        .score-display {{
            font-size: 3em;
            font-weight: 900;
            font-family: 'Playfair Display', serif;
            background: linear-gradient(135deg, #d4af37 0%, #ffd700 50%, #d4af37 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 30px 0;
        }}

        .performance {{
            font-size: 1.5em;
            color: #8b4513;
            margin-bottom: 30px;
            font-family: 'Libre Baskerville', serif;
            font-style: italic;
        }}

        @media (max-width: 768px) {{
            h1 {{ font-size: 2em; }}
            .quiz-header {{ flex-direction: column; }}
        }}
    </style>
</head>
<body>
    <div class="floating-symbols" id="floatingSymbols"></div>

    <div class="container">
        <div class="header">
            <h1>🎪 Mad English ⚡</h1>
            <p class="subtitle">Dynamically Generated Questions!</p>
        </div>

        <div id="quizScreen" class="quiz-container">
            <div class="quiz-header">
                <div class="quiz-info">
                    <div class="info-badge">{category_display}</div>
                    <div class="info-badge">{difficulty_display}</div>
                    <div class="info-badge">Question <span id="questionNum">1</span>/10</div>
                </div>
                <div class="timer" id="timer">⏱️ 0s</div>
            </div>

            <div class="question-container">
                <div class="question-number" id="questionNumber">Question 1 of 10</div>
                <div class="question-text" id="questionText"></div>
                <div class="options" id="options"></div>
            </div>

            <button class="next-btn hidden" id="nextBtn">Next Question →</button>
        </div>

        <div id="resultsScreen" class="quiz-container hidden">
            <div class="results">
                <h2>Quiz Complete! 🎉</h2>
                <div class="score-display" id="finalScore"></div>
                <div class="performance" id="performance"></div>
            </div>
        </div>
    </div>

    <script>
        const questions = {questions_json};
        let currentQuestion = 0;
        let score = 0;
        let startTime = Date.now();
        let timerInterval = null;
        let selectedAnswer = null;

        const quizScreen = document.getElementById('quizScreen');
        const resultsScreen = document.getElementById('resultsScreen');
        const questionNum = document.getElementById('questionNum');
        const timer = document.getElementById('timer');
        const questionNumber = document.getElementById('questionNumber');
        const questionText = document.getElementById('questionText');
        const optionsContainer = document.getElementById('options');
        const nextBtn = document.getElementById('nextBtn');
        const finalScore = document.getElementById('finalScore');
        const performance = document.getElementById('performance');

        // Create floating symbols
        const symbols = ['📚', '✍️', '📖', '📝', '✨', '📕', '🖋️', '📜', '🎓', '💭'];
        const floatingSymbols = document.getElementById('floatingSymbols');
        for (let i = 0; i < 20; i++) {{
            const symbol = document.createElement('div');
            symbol.className = 'symbol';
            symbol.textContent = symbols[Math.floor(Math.random() * symbols.length)];
            symbol.style.left = Math.random() * 100 + '%';
            symbol.style.animationDelay = Math.random() * 20 + 's';
            symbol.style.animationDuration = (15 + Math.random() * 10) + 's';
            floatingSymbols.appendChild(symbol);
        }}

        // Start timer
        timerInterval = setInterval(() => {{
            const elapsed = Math.floor((Date.now() - startTime) / 1000);
            timer.textContent = `⏱️ ${{elapsed}}s`;
        }}, 1000);

        function showQuestion() {{
            const question = questions[currentQuestion];
            selectedAnswer = null;

            questionNum.textContent = currentQuestion + 1;
            questionNumber.textContent = `Question ${{currentQuestion + 1}} of 10`;
            questionText.textContent = question.q;

            optionsContainer.innerHTML = '';
            question.options.forEach((option, index) => {{
                const optionDiv = document.createElement('div');
                optionDiv.className = 'option';
                optionDiv.textContent = option;
                optionDiv.addEventListener('click', () => selectAnswer(index, optionDiv));
                optionsContainer.appendChild(optionDiv);
            }});

            nextBtn.classList.add('hidden');
        }}

        function selectAnswer(index, element) {{
            if (selectedAnswer !== null) return;

            selectedAnswer = index;
            const question = questions[currentQuestion];
            const options = optionsContainer.querySelectorAll('.option');

            element.classList.add('selected');

            setTimeout(() => {{
                options.forEach((opt, i) => {{
                    opt.style.pointerEvents = 'none';
                    if (i === question.answer) {{
                        opt.classList.add('correct');
                    }} else if (i === selectedAnswer) {{
                        opt.classList.add('incorrect');
                    }}
                }});

                if (selectedAnswer === question.answer) {{
                    score++;
                }}

                nextBtn.classList.remove('hidden');
            }}, 300);
        }}

        nextBtn.addEventListener('click', () => {{
            currentQuestion++;
            if (currentQuestion < questions.length) {{
                showQuestion();
            }} else {{
                showResults();
            }}
        }});

        function showResults() {{
            clearInterval(timerInterval);
            const elapsed = Math.floor((Date.now() - startTime) / 1000);

            quizScreen.classList.add('hidden');
            resultsScreen.classList.remove('hidden');

            const percentage = (score / questions.length) * 100;
            finalScore.textContent = `${{score}} / ${{questions.length}}`;

            let performanceText = '';
            if (percentage === 100) {{
                performanceText = '🏆 Perfect! Mad English Master!';
            }} else if (percentage >= 80) {{
                performanceText = '✨ Excellent! Outstanding knowledge!';
            }} else if (percentage >= 60) {{
                performanceText = '📚 Good job! Keep learning!';
            }} else if (percentage >= 40) {{
                performanceText = '📖 Fair! Practice makes perfect!';
            }} else {{
                performanceText = '📝 Keep trying! You can do it!';
            }}

            performanceText += `<br><small>Completed in ${{elapsed}} seconds</small>`;
            performance.innerHTML = performanceText;
        }}

        showQuestion();
    </script>
</body>
</html>"""

        return html

if __name__ == "__main__":
    bot = MadEnglish()
    bot.run()
