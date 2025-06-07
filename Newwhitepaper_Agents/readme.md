0607
    checked google's Newwhitepaper_Agents, here is demo code to run it

    main conclusion:
    1.function_demo is not working, maybe because of GenerativeModel.generate_content  did not prompt new Gemini model well to give a function_call result
        better there is a opensource solution to this, so we can change and fix
    2.extension_demo is working
    3.langChain_demo is working, but not necessaryly run 1 search -> 2 places, sometimes 1 search -> 2 search can also find the result too
        aha moment: once model find 1 search -> 2 places cannot get any places, he try a 3nd time search
            "I was unable to find the address of the Ohio State Buckeyes stadium. I will try a different query."
            check the log in langChain_demo

    some configs to make:
    1.download all dependencis pkg in venv
    source /xxx/venv/bin/activate 
    2.login to google cloud console and add payment info
    3.config for google SerpAPIWrapper and GooglePlacesTool and get api keys