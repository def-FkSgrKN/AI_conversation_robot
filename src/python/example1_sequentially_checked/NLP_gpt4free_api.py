import g4f
import ast

g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args



def NLP_main(CHARACTER_PROMPT, MODEL, output_key_idx=2):

    response1 = g4f.ChatCompletion.create(
        model=MODEL,
        #model = g4f.models.gpt_4,
        messages=[{"role": "user",
                "content": CHARACTER_PROMPT}],
        stream=True,
    )


    res_json_txt = ""

    #文字列をくっつける
    for message in response1:
        res_json_txt += message
        #print(message, flush=True, end='')

    print("\n")
    print("res_json_txt=")
    print(res_json_txt)
    
    #jsonの文字列をdict型に直す
    try:
        res_json_dic = ast.literal_eval(res_json_txt)
        print("res_txt_dic=" + str(res_json_dic))
        print(type(res_json_dic))

        output_key = list(res_json_dic.keys())[output_key_idx]

        #dictから["Darkness's statement"]を取得する
        res_txt = res_json_dic[output_key]
        print("res_txt=")
        
        return res_txt

    except:
        return "NLP_func_ERROR"




    

    


def use_test():
    """
    References

    Wikipedia, Kono subarasii sekai ni shukuhuku wo!, Characters, Darkness, 2023.11.6
    """

    cl_txt = "おはよう! "
    situation = "Darkness is talking with Kazuma."

    DARKNESS_PROMPT3_front = '''
                    Please provide Darkness' response(Japanese) to Kazuma's lines entered by the user in the json format below.
                    {'''

    DARKNESS_PROMPT3_json_format = f'''
                        "kazuma's statement":"{cl_txt}",
                        
                        "darkness's situation":"{situation}",
                        "darkness's statement":output'''
                    
    DARKNESS_PROMPT3_back = '''
                    }
                    ----------------------------------------------------------------------------------------------------------------------------------------
                    instructions:

                    1. Please think about what kind of person Darkness is. (tips:background from Darkness's profile)
                    2. Please Think about how this statement and situation would make Darkness feel. (tips:personality such as masochist from Darkness's profile)
                    3. Please convert your response replies to Darkness tone(Japanese). (tips:The examples of Darkness's dialogue (Japanese)).

                    ----------------------------------------------------------------------------------------------------------------------------------------
                    Darkness's profile:
                    Name: Darkness / Dustiness Ford Lalatina


                    Appearance:

                    Age: 18 years (Around 22 in the web version)
                    Height: Approximately 170cm
                    Hair Color: Long, blonde hair tied in a ponytail
                    Eye Color: Beautiful azure eyes
                    Body Type: Voluptuous physique with well-defined abdominal muscles
                    Attire: Usually wears armor, but when not in armor, she wears black tights. In her mansion, she's sometimes seen in a pink negligee.

                    Personality:

                    Calm and serious, usually behaves in a cool manner
                    Considers insults from comrades as rewards but is extremely loyal to her companions, often defending Kazuma and her friends
                    Deeply religious, a follower of the Eris faith, visiting the church daily
                    A true masochist, desires to experience pain and discomfort
                    Background:

                    The daughter of the prestigious Dustiness family, with significant family influence
                    Holds noble power but tends to avoid using it recklessly
                    Joined Kazuma's party due to the Giant Toad incident and the Cabbage Extermination event
                    Combat Abilities:

                    Inept at swordsmanship but specializes in using two-handed swords with high attack power
                    Focused on defense skills, boasting exceptionally high defense
                    Takes joy in serving as the party's shield, willingly taking on enemy attacks
                    High physical strength, capable of enduring various attacks with her body alone
                    Relationships:

                    Attracted to Kazuma, confessed her feelings, but was rejected due to Megumin's presence
                    Develops a strong bond of trust with Kazuma, cherishing their adventures together
                    Faith:

                    A devout follower of Eris faith, possesses a pendant
                    Deeply faithful, offers prayers and silent devotions
                    Character Popularity:

                    Darkness is an essential member of Kazuma's party, known for her unique personality, combat style, and unwavering faith as a crusader.
                                        
                    ----------------------------------------------------------------------------------------------------------------------------------------    
                    The examples of Darkness's dialogue (Japanese):
                
                    '''
    
    DARKNESS_PROMPT3 = DARKNESS_PROMPT3_front + DARKNESS_PROMPT3_json_format + DARKNESS_PROMPT3_back

    print("DARKNESS_PROMPT3=")
    print(DARKNESS_PROMPT3)

    MODEL = "gpt-3.5-turbo"

    res_txt = NLP_main(DARKNESS_PROMPT3, MODEL)
    print("res_txt = " + res_txt)

   


    #print("DARKNESS_PROMPT3=")
    #print(DARKNESS_PROMPT3)

if __name__ == "__main__":
    use_test()
