"""Textos del sitio en inglés y español. `build.py` genera las páginas con ellos."""

EN = dict(
    title="Chand — Finger strength for climbers",
    description="Measure max finger strength, track fatigue during a session and train with force targets, "
                "using your Bluetooth force sensor. No account, no ads, no tracking.",
    skip="Skip to content", nav_label="Main", footer_label="Footer", lang_label="Versión en español",
    nav_fatigue="Fatigue", nav_measure="Measure", nav_train="Train", nav_privacy="Privacy", nav_support="Support",
    contact="Contact",
    hero_h1="<span>Test. Train.</span><span>Know when to <em>stop</em>.</span>",
    hero_lead="Chand turns your Bluetooth force sensor into a finger strength lab for climbers, on your iPhone.",
    soon="Coming soon to the App Store", how="See how it works",
    facts=["No account", "No ads", "No tracking", "English and Spanish"],
    chip_max="Max strength", chip_loss="Strength loss",
    alt_capture="Chand measuring a max strength pull, with the force curve of each hand.",
    alt_fatigue="Fatigue session: strength lost by each hand against the reference, with the threshold warning.",
    alt_fatigue_chart="Chart of the percentage of the reference kept by each hand, pull after pull.",
    alt_plan="A named measurement: best and latest result per hand and their progress over the weeks.",
    alt_summary="Summary of a saved measurement, with the curve and figures of each hand.",
    alt_workout="An interval workout in progress, with the force target for the current rep.",
    alt_live="Live force with a target zone.",
    reference="Reference", threshold="Threshold", peak="Peak", left="Left", right="Right", target_zone="Target zone",

    fatigue_h2="How much strength is left, in one pull.",
    fatigue_lead="Between blocks, a control pull that takes a few seconds. Chand compares it with your reference "
                 "and shows what you have lost, so you can decide when to stop.",
    verdict_label="With this threshold", verdict_stop="Stop at pull {}",
    threshold_label="Loss threshold",
    fatigue_viz_desc="Eight control pulls, each a little lower than the previous one, against a dotted reference "
                     "line. A second dotted line marks the loss threshold; the pulls below it are highlighted.",
    fatigue_cap="Each bar is a control pull. The top dotted line is your reference; when a pull falls below the "
                "threshold, it is time to stop. Move the threshold to see it change.",
    fatigue_steps=[
        ("Set the reference", "Measure it as you start, or pick a measurement you already have."),
        ("Pull between blocks", "Each control pull shows the loss in peak force and in RFD, for each hand."),
        ("Stop at the threshold", "When the loss goes past the threshold you chose, the app warns you."),
        ("Your records stay clean", "Control pulls never count as tests or change your records."),
    ],

    measure_h2="Every pull, with its curve.",
    measure_lead="Max strength, RFD, endurance and critical force. Each hand on its own or both together, "
                 "with every attempt saved.",
    pull_viz_desc="Force curve of a three-second pull: a fast rise to the peak, a plateau and the release. "
                  "The slope between 20% and 80% of the peak is marked as RFD.",
    pull_cap="The peak is the highest point of the curve. RFD is how fast you get there: the slope between "
             "20% and 80% of the peak.",
    g_peak_t="Peak", g_peak="The highest force of the pull.",
    g_rfd_t="RFD", g_rfd="Rate of force development: kilos per second as the pull starts.",
    g_loss_t="Loss", g_loss="What is missing to reach the reference: <code>100 − value ÷ reference × 100</code>.",
    g_asym_t="Asymmetry", g_asym="The gap between your strong hand and the weak one, relative to the strong one.",
    g_cf_t="Critical force",
    g_cf="24 reps of 7 s with 3 s of rest. The average of the last six is your critical force (CF): "
         "what you can sustain. What you put in above it is your reserve (W′).",

    train_h2="Intervals with a force target.",
    train_lead="Sets with reps, work and rest. The target zone is set in kilos or as a percentage of your max, "
               "and the rep starts when you pull.",
    train_viz_desc="Six reps of seven seconds of work and three of rest. The force trace stays inside a band "
                   "that marks the target zone, between 65% and 75% of the max.",
    train_cap="Six reps of 7 s with 3 s of rest. The band is the target zone: 65–75% of your max with that grip.",
    train_steps=[
        ("Templates", "Save, duplicate, import and export them. Or start a quick workout."),
        ("To failure", "Sets to failure, by reps or by time."),
        ("Live", "Force in real time, with a target zone and tones as you enter it or overshoot."),
    ],

    themes_label="Themes", themes_h2="Six themes, for any gym.",
    themes_lead="From pure black you can read with chalk on the screen to a light background for bright rooms.",
    theme_alt="The Today tab in the {} theme.",
    themes=[("dark", "Dark", "Black and orange. The classic."),
            ("ember", "Ember", "The icon's oranges on dark brown."),
            ("light", "Light", "For brightly lit gyms."),
            ("clean", "Clean", "Black and white, no distractions."),
            ("solarized", "Solarized Dark", "Easy on the eyes."),
            ("contrast", "High contrast", "Readable from afar.")],

    privacy_h2="Your data never leaves your iPhone.",
    privacy_lead="Chand does not collect any data. Everything you record stays on your device, and you export it "
                 "only when you choose to.",
    zeros=[("accounts", "No sign-up and no login."),
           ("trackers", "No analytics and no third-party SDKs."),
           ("ads", "None, anywhere in the app."),
           ("connections", "The app never connects to the internet.")],
    privacy_link="Read the privacy policy", support_link="Support and contact",

    req_label="Requirements", req_h2="What you need.",
    req=[("An iPhone", "With iOS 26 or later."),
         ("A Bluetooth force sensor",
          "Chand works with sensors that use the Tindeq Progressor protocol. Chand is an independent app, "
          "not affiliated with or endorsed by any sensor manufacturer."),
         ("Or nothing at all", "A demo mode lets you explore the app without a sensor.")],
    health="Chand is a measuring and training tool, not a medical device. Maximal pulls put a heavy load on fingers, "
           "pulleys, tendons and shoulders: warm up, stop if you feel pain and consult a professional if you have "
           "an injury or any doubts.",
    site_note="This website uses no cookies, no analytics and no third-party resources.",
    privacy_title="Chand – Privacy policy",
    privacy_description="Chand does not collect any data. Everything you record stays on your iPhone.",
    support_title="Chand – Support",
    support_description="Help, common questions and contact for Chand, the finger strength app for iPhone.",
)

ES = dict(
    title="Chand — Fuerza de dedos para escalar",
    description="Mide tu fuerza máxima de dedos, controla la fatiga durante la sesión y entrena con objetivos de "
                "fuerza, con tu sensor de fuerza Bluetooth. Sin cuenta, sin anuncios y sin seguimiento.",
    skip="Saltar al contenido", nav_label="Principal", footer_label="Pie", lang_label="English version",
    nav_fatigue="Fatiga", nav_measure="Medir", nav_train="Entrenar", nav_privacy="Privacidad", nav_support="Ayuda",
    contact="Contacto",
    hero_h1="<span>Mide. Entrena.</span><span>Decide cuándo <em>parar</em>.</span>",
    hero_lead="Chand convierte tu sensor de fuerza Bluetooth en un laboratorio de fuerza de dedos para escalar, "
              "en tu iPhone.",
    soon="Próximamente en el App Store", how="Cómo funciona",
    facts=["Sin cuenta", "Sin anuncios", "Sin seguimiento", "En español e inglés"],
    chip_max="Fuerza máxima", chip_loss="Pérdida de fuerza",
    alt_capture="Chand midiendo un tirón de fuerza máxima, con la curva de fuerza de cada mano.",
    alt_fatigue="Sesión de fatiga: fuerza perdida por cada mano respecto a la referencia, con el aviso de umbral.",
    alt_fatigue_chart="Gráfica del porcentaje de la referencia que conserva cada mano, tirón a tirón.",
    alt_plan="Una medición con nombre: mejor y último resultado de cada mano y su evolución por semanas.",
    alt_summary="Resumen de una medición guardada, con la curva y los datos de cada mano.",
    alt_workout="Un entreno por intervalos en marcha, con el objetivo de fuerza de la repetición.",
    alt_live="Fuerza en vivo con zona objetivo.",
    reference="Referencia", threshold="Umbral", peak="Pico", left="Izquierda", right="Derecha",
    target_zone="Zona objetivo",

    fatigue_h2="Cuánta fuerza te queda, en un tirón.",
    fatigue_lead="Entre bloque y bloque, un tirón de control de pocos segundos. Chand lo compara con tu referencia "
                 "y te enseña lo que has perdido, para que decidas cuándo parar.",
    verdict_label="Con este umbral", verdict_stop="Para en el tirón {}",
    threshold_label="Umbral de pérdida",
    fatigue_viz_desc="Ocho tirones de control, cada uno algo más bajo que el anterior, frente a una línea de puntos "
                     "de referencia. Otra línea de puntos marca el umbral de pérdida; los tirones que quedan por "
                     "debajo aparecen resaltados.",
    fatigue_cap="Cada barra es un tirón de control. La línea de puntos de arriba es tu referencia; cuando un tirón "
                "queda por debajo del umbral, toca parar. Mueve el umbral para verlo.",
    fatigue_steps=[
        ("Fija la referencia", "Mídela al empezar o elige una medición que ya tengas."),
        ("Tira entre bloques", "Cada tirón de control muestra la pérdida de pico y de RFD, por mano."),
        ("Para en el umbral", "Cuando la pérdida supera el umbral que has elegido, la app te avisa."),
        ("Tus récords, intactos", "Los tirones de control no cuentan como tests ni alteran tus récords."),
    ],

    measure_h2="Cada tirón, con su curva.",
    measure_lead="Fuerza máxima, RFD, resistencia y fuerza crítica. Cada mano por separado o las dos a la vez, "
                 "con todos los intentos guardados.",
    pull_viz_desc="Curva de fuerza de un tirón de tres segundos: subida rápida hasta el pico, meseta y suelta. "
                  "La pendiente entre el 20 % y el 80 % del pico está marcada como RFD.",
    pull_cap="El pico es el punto más alto de la curva. El RFD es lo rápido que llegas: la pendiente entre el "
             "20 % y el 80 % del pico.",
    g_peak_t="Pico", g_peak="La fuerza más alta del tirón.",
    g_rfd_t="RFD", g_rfd="Velocidad de desarrollo de la fuerza: kilos por segundo en el arranque del tirón.",
    g_loss_t="Pérdida", g_loss="Lo que falta para llegar a la referencia: <code>100 − valor ÷ referencia × 100</code>.",
    g_asym_t="Asimetría", g_asym="La diferencia entre tu mano fuerte y la débil, respecto a la fuerte.",
    g_cf_t="Fuerza crítica",
    g_cf="24 repeticiones de 7 s con 3 s de descanso. La media de las seis últimas es tu fuerza crítica (CF): "
         "lo que puedes sostener. Lo que pones por encima es tu reserva (W′).",

    train_h2="Intervalos con objetivo de fuerza.",
    train_lead="Series con repeticiones, trabajo y descanso. La zona objetivo va en kilos o en porcentaje de tu "
               "máxima, y la repetición empieza cuando tiras.",
    train_viz_desc="Seis repeticiones de siete segundos de trabajo y tres de descanso. La traza de fuerza se "
                   "mantiene dentro de una banda que marca la zona objetivo, entre el 65 % y el 75 % de la máxima.",
    train_cap="Seis repeticiones de 7 s con 3 s de descanso. La banda es la zona objetivo: el 65–75 % de tu máxima "
              "con ese agarre.",
    train_steps=[
        ("Plantillas", "Guárdalas, duplícalas, impórtalas y expórtalas. O empieza un entreno rápido."),
        ("Hasta el fallo", "Series hasta el fallo, por repeticiones o por tiempo."),
        ("En vivo", "La fuerza en tiempo real, con zona objetivo y tonos al entrar y al pasarte."),
    ],

    themes_label="Temas", themes_h2="Seis temas, para cualquier sala.",
    themes_lead="Del negro puro que se lee con magnesio en la pantalla al fondo claro para salas con mucha luz.",
    theme_alt="La pestaña Hoy con el tema {}.",
    themes=[("dark", "Oscuro", "Negro y naranja. El de siempre."),
            ("ember", "Brasa", "Los naranjas del icono sobre marrón."),
            ("light", "Claro", "Para salas con mucha luz."),
            ("clean", "Limpio", "Blanco y negro, sin distracciones."),
            ("solarized", "Solarized Dark", "Descansado para la vista."),
            ("contrast", "Alto contraste", "Se lee desde lejos.")],

    privacy_h2="Tus datos no salen de tu iPhone.",
    privacy_lead="Chand no recoge ningún dato. Todo lo que registras se queda en tu dispositivo y solo lo exportas "
                 "cuando tú lo decides.",
    zeros=[("cuentas", "Sin registro ni inicio de sesión."),
           ("rastreadores", "Sin analítica ni componentes de terceros."),
           ("anuncios", "Ninguno, en ninguna parte de la app."),
           ("conexiones", "La app nunca se conecta a internet.")],
    privacy_link="Leer la política de privacidad", support_link="Ayuda y contacto",

    req_label="Requisitos", req_h2="Lo que necesitas.",
    req=[("Un iPhone", "Con iOS 26 o posterior."),
         ("Un sensor de fuerza Bluetooth",
          "Chand funciona con los sensores que usan el protocolo del Tindeq Progressor. Chand es una app "
          "independiente, sin relación con ningún fabricante de sensores ni respaldada por ellos."),
         ("O nada", "El modo demo permite conocer la app sin sensor.")],
    health="Chand es una herramienta de medición y entrenamiento, no un producto sanitario. Tirar a fuerza máxima "
           "carga mucho los dedos, las poleas, los tendones y los hombros: calienta, para si notas dolor y consulta "
           "con un profesional si tienes una lesión o dudas.",
    site_note="Esta web no usa cookies, analítica ni recursos de terceros.",
    privacy_title="Chand – Política de privacidad",
    privacy_description="Chand no recoge ningún dato. Todo lo que registras se queda en tu iPhone.",
    support_title="Chand – Ayuda y contacto",
    support_description="Ayuda, preguntas frecuentes y contacto de Chand, la app de fuerza de dedos para iPhone.",
)

LANGS = {"en": EN, "es": ES}

# Política de privacidad y ayuda: el texto es el publicado con la app.
PAGES = {
    "privacy": {
        "en": """<p class="label">Privacy</p>
<h1>Privacy policy</h1>
<p class="meta">Chand for iPhone · Last updated: 14 November 2026</p>
<p class="key"><strong>Chand does not collect any data.</strong> The app has no accounts, no analytics, no advertising and no third-party SDKs, and it never connects to the internet.</p>
<h2>What the app stores</h2>
<p>Everything you record stays on your iPhone, inside the app: measurements and force curves, sessions, workouts, grips, templates, and the settings and profile you enter (name, body weight, dominant hand). None of it is sent to the developer or to anyone else.</p>
<p>If you have iCloud Backup or an encrypted computer backup enabled, Apple includes the app's data in your device backup, under your own Apple account.</p>
<h2>Bluetooth</h2>
<p>Chand uses Bluetooth only to connect to your force sensor and read force and battery values from it. It does not use Bluetooth to determine your location or to detect other devices.</p>
<h2>Exporting and sharing</h2>
<p>You can export your settings (JSON) and results (CSV), or share an image of a result. This only happens when you choose to, through the iOS share sheet, and the file goes wherever you send it.</p>
<h2>Deleting your data</h2>
<p>You can delete individual items inside the app. Deleting the app from your iPhone removes all of its data.</p>
<h2>Children</h2>
<p>The app is not directed at children and collects no data from anyone.</p>
<h2>This website</h2>
<p>This website uses no cookies, no analytics and no third-party resources, and it stores nothing in your browser. It is hosted on GitHub Pages; as with any website, the hosting provider receives your IP address in order to serve the pages.</p>
<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with its date.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="{issues}">open an issue on GitHub</a>.</p>""",
        "es": """<p class="label">Privacidad</p>
<h1>Política de privacidad</h1>
<p class="meta">Chand para iPhone · Última actualización: 14 de noviembre de 2026</p>
<p class="key"><strong>Chand no recoge ningún dato.</strong> La app no tiene cuentas, ni analítica, ni publicidad, ni componentes de terceros, y nunca se conecta a internet.</p>
<h2>Qué guarda la app</h2>
<p>Todo lo que registras se queda en tu iPhone, dentro de la app: mediciones y curvas de fuerza, sesiones, entrenos, agarres, plantillas, y los ajustes y el perfil que escribas (nombre, peso corporal, mano dominante). Nada de eso se envía al desarrollador ni a nadie.</p>
<p>Si tienes activada la copia de seguridad de iCloud o una copia cifrada en el ordenador, Apple incluye los datos de la app en la copia de tu dispositivo, bajo tu propia cuenta de Apple.</p>
<h2>Bluetooth</h2>
<p>Chand usa Bluetooth solo para conectarse a tu sensor de fuerza y leer de él la fuerza y la batería. No lo usa para conocer tu ubicación ni para detectar otros dispositivos.</p>
<h2>Exportar y compartir</h2>
<p>Puedes exportar la configuración (JSON) y los resultados (CSV), o compartir la imagen de un resultado. Solo ocurre cuando tú lo decides, con la hoja de compartir de iOS, y el archivo va a donde tú lo envíes.</p>
<h2>Borrar tus datos</h2>
<p>Puedes borrar cada elemento desde la app. Al eliminar la app del iPhone se borran todos sus datos.</p>
<h2>Menores</h2>
<p>La app no está dirigida a menores y no recoge datos de nadie.</p>
<h2>Esta web</h2>
<p>Esta web no usa cookies, analítica ni recursos de terceros, y no guarda nada en tu navegador. Está alojada en GitHub Pages; como con cualquier web, el proveedor de alojamiento recibe tu dirección IP para poder servir las páginas.</p>
<h2>Cambios</h2>
<p>Si esta política cambia, la versión nueva se publicará en esta página con su fecha.</p>
<h2>Contacto</h2>
<p>Dudas sobre privacidad: <a href="{issues}">abre una incidencia en GitHub</a>.</p>""",
    },
    "support": {
        "en": """<p class="label">Support</p>
<h1>Support</h1>
<p class="meta">Chand for iPhone</p>
<h2>Contact</h2>
<p>To report a problem or ask a question, <a href="{issues}">open an issue on GitHub</a>. Please include the app version (Settings → About), your iPhone model and iOS version, and the steps that lead to the problem.</p>
<p class="contact"><a class="pill" href="{issues}">Open an issue</a></p>
<h2>Common questions</h2>
<details><summary>Which sensors work?</summary><p>Chand works with Bluetooth force sensors that use the Tindeq Progressor protocol. Chand is an independent app and is not affiliated with or endorsed by any sensor manufacturer.</p></details>
<details><summary>The sensor does not connect.</summary><p>Turn the sensor on, make sure Bluetooth is on and that Chand has Bluetooth permission (iOS Settings → Chand), close the manufacturer's app if it is connected to the sensor, and tap “Connect sensor” on the Today tab.</p></details>
<details><summary>Can I try the app without a sensor?</summary><p>Yes. Turn on Settings → No sensor → Demo mode. “Connect sensor” then connects to a simulated sensor and a “Simulate pull” button appears on the measuring screens.</p></details>
<details><summary>How do I back up or move my data?</summary><p>Settings → Data exports the configuration (grips, named measurements, templates and settings) as a JSON file that can be imported again. Results are exported as CSV from the full history.</p></details>
<details><summary>How do I change the language?</summary><p>The app follows your iPhone's language (English or Spanish). To choose one just for Chand, go to Settings → Language.</p></details>
<h2>Health notice</h2>
<p>Chand is a measuring and training tool, not a medical device. Maximal pulls put a heavy load on fingers, pulleys, tendons and shoulders: warm up, stop if you feel pain and consult a professional if you have an injury or any doubts. You use the app at your own risk.</p>
<p><a href="privacy.html">Privacy policy</a></p>""",
        "es": """<p class="label">Ayuda</p>
<h1>Ayuda y contacto</h1>
<p class="meta">Chand para iPhone</p>
<h2>Contacto</h2>
<p>Para avisar de un problema o preguntar algo, <a href="{issues}">abre una incidencia en GitHub</a>. Indica la versión de la app (Ajustes → Acerca de), el modelo de iPhone y la versión de iOS, y los pasos que llevan al problema.</p>
<p class="contact"><a class="pill" href="{issues}">Abrir una incidencia</a></p>
<h2>Preguntas frecuentes</h2>
<details><summary>¿Qué sensores sirven?</summary><p>Chand funciona con sensores de fuerza Bluetooth que usan el protocolo del Tindeq Progressor. Chand es una app independiente, sin relación con ningún fabricante de sensores ni respaldada por ellos.</p></details>
<details><summary>El sensor no conecta.</summary><p>Enciende el sensor, comprueba que el Bluetooth está activado y que Chand tiene permiso de Bluetooth (Ajustes de iOS → Chand), cierra la app del fabricante si está conectada al sensor y pulsa «Conectar sensor» en la pestaña Hoy.</p></details>
<details><summary>¿Puedo probar la app sin sensor?</summary><p>Sí. Activa Ajustes → Sin sensor → Modo demo. «Conectar sensor» conecta entonces con un sensor simulado y aparece el botón «Simular tirón» en las pantallas de medición.</p></details>
<details><summary>¿Cómo guardo o traslado mis datos?</summary><p>Ajustes → Datos exporta la configuración (agarres, mediciones con nombre, plantillas y ajustes) en un archivo JSON que se puede volver a importar. Los resultados se exportan en CSV desde el historial completo.</p></details>
<details><summary>¿Cómo cambio el idioma?</summary><p>La app sigue el idioma del iPhone (español o inglés). Para elegir uno solo para Chand, entra en Ajustes → Idioma.</p></details>
<h2>Aviso de salud</h2>
<p>Chand es una herramienta de medición y entrenamiento, no un producto sanitario. Tirar a fuerza máxima carga mucho los dedos, las poleas, los tendones y los hombros: calienta, para si notas dolor y consulta con un profesional si tienes una lesión o dudas. Usas la app bajo tu propia responsabilidad.</p>
<p><a href="privacy.html">Política de privacidad</a></p>""",
    },
}
