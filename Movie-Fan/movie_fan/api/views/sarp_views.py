import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
# from serpapi import GoogleSearch
from decouple import config
from dotenv import load_dotenv

class MovieView(APIView):
    def get(self, request):
        # load_dotenv()
        # SERP_API_KEY = config('SERP_API_KEY', default='default_value_if_not_present')

        query = request.GET.get('q')
        # if not query:
        #     return Response({'movies': []}, status=status.HTTP_200_OK)
        
        # url = f'https://serpapi.com/search.json?engine=google_play_movies&q={query}'
        

        # params = {
        #     "engine": "google_play_movies",
        #     "q": f"{query}",
        #     "api_key": f'{SERP_API_KEY}',
        # }

        # try:
        #     response = requests.get(url, params=params)
        #     data = response.json()
        #     data = data.get('organic_results')[0].get('items')
        #     # data = json.loads(data).get('organic_results')
        #     return Response({'movies': data}, status=status.HTTP_200_OK)
        # except:
        #     return Response({'movies': []}, status=status.HTTP_200_OK)

        return Response({'movies': [
        {
            "title": "Just Friends",
            "link": "https://play.google.com/store/movies/details/Just_Friends?id=wjTdZJVMi4I",
            "product_id": "wjTdZJVMi4I",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=wjTdZJVMi4I&sort_by=1",
            "rating": 4.3,
            "maturity_rating": "PG-13",
            "category": "Comedy",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/T2Isz1Y4m7aH1sh1uZRbaubRQPnut4oSwIM3MujPrHvWEDgN0ZJX2JFZXSENegoyUao6yQ=s256-rw",
            "description": "Chris (Reynolds) was an overweight nerd and in love with his best friend Jamie (Smart), but she only thought of him like a brother. Ten years later, Chris is now a hot L.A. music exec and finds himself himself back in his hometown and in love with Jamie all over again."
        },
        {
            "title": "Thomas & Friends: The Christmas Engines",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_The_Christmas_Engines?id=w2sR44l74F4",
            "product_id": "w2sR44l74F4",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=w2sR44l74F4&sort_by=1",
            "rating": 4.1,
            "maturity_rating": "TV-Y",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:jpfLCaT2PiE?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/evwZ5p8ONmsDnY3JFIYaumO4zL4Nl6N8NjeiTxaiiXO2HhnV46PeQ0SxS0s8SKjhAfjg=s256-rw",
            "description": "Thomas and his friends are in holly, jolly Christmas spirits, ready to be Santa's engine helpers! Percy brings holiday fun to Reg at the scrapyard, while Duncan tries to overcome his bah humbug attitude. Thomas clears the snowy tracks so Connor can race passengers home in time for the holidays. James causes confusion and delay helping Duck get unstuck, as an old friend returns to Sodor bringing Percy the perfect gift. Join Thomas & Friends as they deliver holiday cheer! (Original Title - Thomas & Friends: The Christmas Engines)"
        },
        {
            "title": "Friends With Kids",
            "link": "https://play.google.com/store/movies/details/Friends_With_Kids?id=y6ILDBGwW78",
            "product_id": "y6ILDBGwW78",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=y6ILDBGwW78&sort_by=1",
            "rating": 3.9,
            "maturity_rating": "R",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:HB5nuVv1PoA?autoplay=1&embed=play",
            "category": "Comedy",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/d0XCynl3BcQAqwOYh3oSqHFF0DzrBQbx1W1U5FDWLpVbzlluuLWijMP7pFhXWc_B3K9mNw=s256-rw",
            "description": "Kristen Wiig, Maya Rudolph and Jon Hamm star alongside Jennifer Westfeldt and Adam Scott in is a daring and hilarious ensemble comedy about a close-knit circle of friends whose lives change once they have kids. The last two singles in the group (Westfeldt and Scott) observe the effect that kids have had on their friends' relationships and wonder if there's a better way to make it work. When they decide to have a child together - and date other people, their unconventional 'experiment' leads everyone in the group to question the nature of friendship, family and, above all, true love. Also starring Chris O'Dowd, Megan Fox and Edward Burns, FRIENDS WITH KIDS delivers the laughs and the heart from beginning to end!"
        },
        {
            "title": "Friends",
            "link": "https://play.google.com/store/movies/details/Friends?id=Fsau_5hVUBo",
            "product_id": "Fsau_5hVUBo",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=Fsau_5hVUBo&sort_by=1",
            "rating": 4.3,
            "maturity_rating": "R",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:bcrhW8K5pXo?autoplay=1&embed=play",
            "category": "Drama",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/UOMJMCvqgC1VB3PnArk6A8ukL4QmPlPwQf5Pwe0Hyt2olDSZUKXK4DNnGNPgtQO1-tSAiw=s256-rw",
            "description": "With one of their fathers recently deceased and the other hardly there, fate brings fifteen-year-old Paul and fourteen-year-old Michelle together in a chance encounter. Instant friends, the young couple flees Paris on a whim, and takes refuge in a rural cottage. But as their fondness for each other blossoms into deep affection, their short trip becomes longer and their love deeper."
        },
        {
            "title": "Friends With Money",
            "link": "https://play.google.com/store/movies/details/Friends_With_Money?id=Ljhzqo8oQcA",
            "product_id": "Ljhzqo8oQcA",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=Ljhzqo8oQcA&sort_by=1",
            "rating": 3.8,
            "maturity_rating": "R",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:CpOQwIo6NSc?autoplay=1&embed=play",
            "category": "Comedy",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/so2w2DxVVF8KKkmdhNOuPZJPO8BUOJAYjj_2KoW0Sfv--X1JLvji1WSdX-6f7Wf_1BA=s256-rw",
            "description": "Jennifer Aniston, Catherine Keener, Frances McDormand and Joan Cusak star in a film the New York Times hails as \"a bittersweet comedy about the drama of being alive...\" -- Manohla Dargis/New York Times, FRIENDS WITH MONEY -- the story of four best friends whose comfortable lives are thrown off balance as the realities of early middle age set in. It paints a painfully hilarious portrait of modern life in the class-sensitive West side of Los Angeles. Written and directed by Nicole Holofcener (Lovely and Amazing), Friends With Money was the Opening Night Selection at the 2006 Sundance Film Festival and is being hailed as \"Terrific\" -- Kenneth Turan/Los Angeles Times, \"Acutely perceptive and slyly quick-witted\" -- Allison Benedikt/Chicago Tribune. (Original Title - Friends With Money) © 2006 Sony Pictures Classics Inc. (for the Universe excluding Australia/NZ and Scandinavia, but including Iceland).  All Rights Reserved."
        },
        {
            "title": "Friends Effing Friends Effing Friends",
            "link": "https://play.google.com/store/movies/details/Friends_Effing_Friends_Effing_Friends?id=1aCAa9hrolE",
            "product_id": "1aCAa9hrolE",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=1aCAa9hrolE&sort_by=1",
            "rating": 5.0,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:9V_O3qW7TBA?autoplay=1&embed=play",
            "category": "Comedy",
            "price": "$2.99",
            "extracted_price": 2.99,
            "thumbnail": "https://play-lh.googleusercontent.com/tUQffbLhjO73_sIg8gjAAvzac-bmKjcpx55rnm97eYiZO2DeYpeoCsPZlwl9FxuoLUT0=s256-rw",
            "description": "Jacob, a freelance copy editor from Los Angeles, struggles to find love as he clings to the carefree, selfish ways of his youth. With the help from his best friends, Steve and Laura, a couple who are going through their own troubles, Jacob is begrudgingly set up with Sarah, a writer in need of an editor. Jacob and Sarah hit it off immediately, however, when Jacob is invited over for a dinner, he meets Sarah’s wild and beautiful roommate, Camille, who’s about to move out of town. Desperate to “get to know her” before she leaves his life forever, Jacob overplays his hand, once again stirring up the pot before the water has even been poured. As things fall apart within personal relationships, one thing leads to another, snowballing out of control, and no one is safe. Recklessly blurring the lines of friendship and sex amongst friends, the conflict becomes Man versus Man as each Friend tries to find love within the group, all while internally battling their own egos to find happiness."
        },
        {
            "title": "Thomas & Friends: New Friends for Thomas & Other Adventures",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_New_Friends_for_Thomas_Other_Advent?id=mD80lHT3DqI",
            "product_id": "mD80lHT3DqI",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=mD80lHT3DqI&sort_by=1",
            "rating": 4.6,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:Vgr1px3Gnyk?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/M7O7JcKxRI1WOtkWvhsVvWYQyWu2paYGIklw4IdAv2WEBvHbrL_823pw17tzegestb0A=s256-rw",
            "description": "It's so busy on the island of Sodor that Sir Topham Hatt needs to bring in some new engines to keep the railway running smoothly. That means new friends and new adventures for Thomas. Climb aboard and meet them all. There is Spencer, the fastest express engine that the island has ever seen. Meet Emily, the sleek green engine with the beautiful brass dome; and new friend Arthur, whose spotlessrecord gets ruined when Thomas plays a trick on him. Don't forget cheerful tractor Jack and all his construction crew friends. And come meet the big and mighty Murdoch, who is always looking for some peace and quiet, but who finds out what it means to have some Really Useful friends. Join Thomas and his new friends for trainloads of discovery and fun. Peep Peep! Includes Bonus Train!"
        },
        {
            "title": "The Friends of Eddie Coyle",
            "link": "https://play.google.com/store/movies/details/The_Friends_of_Eddie_Coyle?id=LcyAMPYpNm8",
            "product_id": "LcyAMPYpNm8",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=LcyAMPYpNm8&sort_by=1",
            "rating": 4.6,
            "maturity_rating": "R",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:vWdqoPHW-F8?autoplay=1&embed=play",
            "category": "Drama",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/x3gpaO7EtaVT8yVfh05dyAzO_Y_p4ntcn1e8U7GJUVYG1h2oinfOdP_lZeZbDWWI3QkqhQ=s256-rw",
            "description": "Based on the best-selling novel by George V. Higgins, The Friends of Eddie Coyle chronicles the last days of a weary Boston-based weapons dealer. Eddie Coyle (Robert Mitchum) doesn't want to serve a life sentence in prison, so he becomes an informant for both the police and the treasury department. Coyle is likewise unwilling to give up his lifestyle, thus he continues his illegal gun-running operation for the underworld. The mob becomes aware that Eddie is squealing to the cops, so they send his best friend, Dillon (Peter Boyle), to rub him out. Dillon compassionately takes Eddie out on the town, treating him to dinner and a hockey game...then drives to a deserted field to carry out his orders."
        },
        {
            "title": "Thomas & Friends: King of the Railway",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_King_of_the_Railway?id=vkkyLBqVUpE",
            "product_id": "vkkyLBqVUpE",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=vkkyLBqVUpE&sort_by=1",
            "rating": 4.2,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:mydtid3JEaw?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/CTzxdcIs_lGKjg2uYI6z0rLbt9fJS30D_R0KRahHnIW01cXeEdpZOIUPjbuUtctoZeA=s256-rw",
            "description": "Join Thomas & Friends™ as they embark on a legendary movie adventure! The steam team's quest begins when a special guest arrives on Sodor with a big surprise and important jobs for Thomas, Percy and James. The engines meet new friends and discover suits of armor; coats of arms and legends of long-ago heroes. Then their bravery is put to the test when their new friend Stephen goes missing. Will Thomas find him in time? Will the engines discover the truth about the Island of Sodor's biggest mystery? It's a crusade of knightly proportions for Thomas & Friends™ in this epic movie!"
        },
        {
            "title": "Friends With Benefits",
            "link": "https://play.google.com/store/movies/details/Friends_With_Benefits?id=RF1A96PtjOg",
            "product_id": "RF1A96PtjOg",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=RF1A96PtjOg&sort_by=1",
            "rating": 4.3,
            "maturity_rating": "R",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:wMVO79F9jSk?autoplay=1&embed=play",
            "category": "Comedy",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/nGKUi9ip7VXhEyV2bCZ_VS94KZkcw_coBc6f7e40JAIFJgJe1eJGQEbq2puhi0rgYH_l=s256-rw",
            "description": "When two friends decide to try something new and take advantage of their mutual attraction without any emotional attachment, they soon realize romantic comedy stereotypes might exist for a reason. (Original Title - Friends With Benefits) © 2011 Screen Gems, Inc. All Rights Reserved."
        },
        {
            "title": "Thomas & Friends: Tales On the Rails",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_Tales_On_the_Rails?id=VOstnOtAj4A",
            "product_id": "VOstnOtAj4A",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=VOstnOtAj4A&sort_by=1",
            "rating": 4.1,
            "maturity_rating": "TV-Y",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:Jc9rr2t3MYc?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/-9mvzeznYc-oCqHcvGFSN2NDxLP9H6G8Zp4wHAmSUdoN69cuUgKgvySgjzU_HKwtZPxR=s256-rw",
            "description": "Thomas and his friends are telling tales on the rails! Percy's sheep escape, as Den and Dart fear working apart. James can't handle the slip coaches, while Salty's imagination has him running scared. When Percy loses control, he bravely faces his fears with a little help from his friends. Track down exciting stories with Thomas and his friends! (Original Title - Thomas & Friends: Tales On the Rails) - 2015 Gullane (Thomas) Limited. All Rights Reserved."
        },
        {
            "title": "Thomas & Friends: Tale of the Brave - The Movie",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_Tale_of_the_Brave_The_Movie?id=IM1_szYi_k0",
            "product_id": "IM1_szYi_k0",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=IM1_szYi_k0&sort_by=1",
            "rating": 4.2,
            "maturity_rating": "TV-Y",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:dsAPEdYmAMo?autoplay=1&embed=play",
            "category": "Family",
            "price": "$3.79",
            "extracted_price": 3.79,
            "thumbnail": "https://play-lh.googleusercontent.com/saOQUM7udzUFkFHemBb4-cPG_MD0XJfwc9CjhVwvDCE8VbMkvNlvFQTYs1G268F_Z9WI=s256-rw",
            "description": "Thomas and his friends face their fears in their boldest adventure yet! After a monstrous storm on the Island of Sodor, a landslide unearths some very unusual footprints. Thomas and Percy are eager to find out what could have made these marks but obstacles and danger seem to appear around every bend in the track. With the help of new friends, a little digging, and a heap of courage, they discover the surprising answer and, along the way, uncover the true meaning of bravery. Join Thomas & Friends in this exciting and inspiring movie adventure. (Original Title - Thomas & Friends: Tale of the Brave - The Movie)"
        },
        {
            "title": "Thomas & Friends: Ultimate Friendship Adventures",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_Ultimate_Friendship_Adventures?id=3lWfkMh9wbU",
            "product_id": "3lWfkMh9wbU",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=3lWfkMh9wbU&sort_by=1",
            "rating": 4.2,
            "maturity_rating": "TV-Y",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:j_zZanXYx_A?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/loeuPqRrhKUIYfvQ-pOk8aQqWXhR8g_OIKpjUA0VZ2nvtuCOv8QohzSm1jaTprhlel50=s256-rw",
            "description": "Double up on your delivery of Thomas & Friends™ with 10 action-packed stories! All aboard for exciting rescues, engines tuning up and flocks of new friends. Learn how to work together, build new friendships and ride the roads or rails for a rainbow of adventure. (Original Title - Thomas & Friends: Ultimate Friendship Adventures) - 2016 Universal Studios. All Rights Reserved."
        },
        {
            "title": "Thomas & Friends: The Great Race - The Movie",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_The_Great_Race_The_Movie?id=JFwIMrpmX18",
            "product_id": "JFwIMrpmX18",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=JFwIMrpmX18&sort_by=1",
            "rating": 4.6,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:awSJ8uWnFlc?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/MKoCZVImt-2OxQR2vRBT66tEhSBqsMFwo5mDuZyZMgniAWrE1v9hphZpk4SBxsjVnDuSmg=s256-rw",
            "description": "Get ready, get set, GO! When the best engines from around the world gather to compete in The Great Railway Show, Thomas is determined to find a way to represent Sodor. But he’s left disappointed as Gordon is chosen to be the new “Shooting Star” for The Great Race. With Gordon and the other engines making the journey to compete, something suddenly goes terribly wrong… and Gordon is in danger! Will Thomas get to the mainland in time to help him and save the day? Join Thomas and his new international friends in this high-speed musical adventure where friendship always wins! (Original Title - Thomas & Friends: The Great Race - The Movie) - 2016 Universal City Studios. All Rights Reserved."
        },
        {
            "title": "Thomas & Friends: James Goes Buzz Buzz",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_James_Goes_Buzz_Buzz?id=9tZtoRXU7uw",
            "product_id": "9tZtoRXU7uw",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=9tZtoRXU7uw&sort_by=1",
            "rating": 3.9,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:nmSU5l_eKdQ?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/0nOTvt9s90BqWzhKRya6sjbALjgQMf8gTOC8t7YbR8-AUzWVdl5dmi5-IoyiwMNtctM=s256-rw",
            "description": "James boasts about his bravery but, when a swarm of bees start buzzing around him he wishes that they would get back to making honey and leave him to make steam. See what happens when Bill and Ben have trouble on the turntable and end up face to face. Climb aboard as we clear the way for trainloads of fun."
        },
        {
            "title": "Thomas & Friends: A Big Day For Thomas",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_A_Big_Day_For_Thomas?id=2h0BM82YOU0",
            "product_id": "2h0BM82YOU0",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=2h0BM82YOU0&sort_by=1",
            "rating": 4.7,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:luEHzUxQtZY?autoplay=1&embed=play",
            "category": "Animation",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/3RCCaBVbjsGLNqzCK_Hbf30adKUEXAyAjtx_7H8rk_4Cg5wsaC_udvJwtGhuANmF2Wci=s256-rw",
            "description": "It's Thomas the Tank Engine, and he's ready to take you on another journey filled with exciting adventures of the Island of Sodor. Travel with Thomas when he gets to pull his very own train for the first time - - with unexpected results. Find out what really \"shocks\" Percy and hold your breath when some snow jams one of the Island's signals and leads Henry to disaster. It's your Big Day, so get ready to join Thomas, James, Toby and the rest of your friends for non-stop fun. All Aboard!"
        },
        {
            "title": "Worst Friends",
            "link": "https://play.google.com/store/movies/details/Worst_Friends?id=9fUOIE4AMNo",
            "product_id": "9fUOIE4AMNo",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=9fUOIE4AMNo&sort_by=1",
            "rating": 2.8,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:ZNSLkgX-Djc?autoplay=1&embed=play",
            "category": "Comedy",
            "price": "$1.99",
            "extracted_price": 1.99,
            "thumbnail": "https://play-lh.googleusercontent.com/B75CfMsctwR4nEtOw4dT0AaSyM3fOc3d_VvUwVVtOp01Yw0uzBORsgn0L2fNKn5AY7cs=s256-rw",
            "description": "When self-involved prankster Jake (Richard Tanne) gets hit by a car, the only person around to take care of him is his childhood friend Sam (Noah Barrow). With the help of pretty, no-nonsense physical therapist Lily (Cody Horn, MAGIC MIKE), Sam agrees to help Jake recover, but when Sam's high school crush Zoe (Kristen Connolly, HOUSE OF CARDS) moves back to town, it's every man for himself and Sam is left asking, \"with friends like these, who needs enemies?!”"
        },
        {
            "title": "Thomas & Friends: Sodor’s Legend of the Lost Treasure - The Movie",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_Sodor_s_Legend_of_the_Lost_Treasure?id=CyhM2SQpWSw",
            "product_id": "CyhM2SQpWSw",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=CyhM2SQpWSw&sort_by=1",
            "rating": 4.5,
            "video": "https://play.google.com/video/lava/web/player/yt:movie:0etZws5Liss?autoplay=1&embed=play",
            "category": "Action & adventure",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/anx3rXxl4IR1aJopN66gUK-3mmledjjc8iNCGHIQnfnY8n_aFHkN-QVag0q_QogZ2TSQBA=s256-rw",
            "description": "Shiver me timbers! Surprises await Thomas and his friends as they dig up their most daring adventure yet. Unearthing an old pirate ship, Thomas is on the hunt for Sodor’s lost treasure. When Thomas rocks the boat with some new friends, trouble soon rushes in. Will Thomas track down the treasure in time or will Sailor John set sail with it? Join Thomas & Friends in this explosive movie adventure!"
        },
        {
            "title": "Thomas & Friends: Start Your Engines!",
            "link": "https://play.google.com/store/movies/details/Thomas_Friends_Start_Your_Engines?id=5iIOs4yAQSI",
            "product_id": "5iIOs4yAQSI",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=5iIOs4yAQSI&sort_by=1",
            "rating": 4.6,
            "maturity_rating": "TV-Y",
            "video": "https://play.google.com/video/lava/web/player/yt:movie:Vn4Y-Pi8rak?autoplay=1&embed=play",
            "category": "Action & adventure",
            "price": "$3.99",
            "extracted_price": 3.99,
            "thumbnail": "https://play-lh.googleusercontent.com/oGJdfqZFXXd5Q93Pr2o_9QG0tY9hIlh8CU5ZjPYmDcNMl6Js23zmF1m6yHoTL7nHvWtk=s256-rw",
            "description": "Thomas & Friends are racing on the rails! The clock is ticking for Thomas, Bertie and Spencer to get to the castle on time. As Philip shows Gordon how fast he can go, slow Stephen proves he can save the day. James and Thomas are on opposite tracks when the Big Game comes to Sodor, while Caitlin gives Emily an unexpected boost. Race down the tracks with Thomas and his friends! (Original Title - Thomas & Friends: Start Your Engines!) - 2016 Gullane (Thomas) Limited."
        },
        {
            "title": "Happy Tree Friends: Still Alive",
            "link": "https://play.google.com/store/movies/details/Happy_Tree_Friends_Still_Alive?id=OnC3CixZFWU",
            "product_id": "OnC3CixZFWU",
            "serpapi_link": "https://serpapi.com/search.json?engine=google_play_product&gl=us&hl=en&platform=phone&product_id=OnC3CixZFWU&sort_by=1",
            "rating": 4.2,
            "category": "Comedy",
            "price": "$5.99",
            "extracted_price": 5.99,
            "thumbnail": "https://play-lh.googleusercontent.com/4FOtryeHSY9PvBDIsnC1weA-T3xzK2JGXXA2IN9yhbuucZ9WzkIZGHV6TXK06tL0uB3L=s256-rw",
            "description": "It's been years since we've last seen the Happy Tree Friends gang. Some say they had fallen out of internet obscurity. Others, that they were trapped in an Error 404 page, never to escape. In some corners, there were whispers - rumors that they might be (gasp!) DEAD! Fear not, true believers! Happy Tree Friends is back and very much Still Alive!!!"
        }
    ]}, status=status.HTTP_200_OK)

