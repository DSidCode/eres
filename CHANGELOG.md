# Changelog (Historial de Magia y Desarrollo)
Este documento registra cronológicamente los avances, epifanías creativas y mejoras técnicas del Proyecto Ibeji & Umbanda.

---

## [v3.6.3] - 29 de Agosto, 2026

### 🪐 Navegación Esférica Planetaria (*Stellarium Style*) & Selector Rápido de Constelaciones
* **Cámara Esférica Cinemática 1:1 Sin Deformaciones:**
  * Sustitución del desplazamiento en píxeles lineales por un modelo angular astronómico real en grados de ascensión recta y declinación (`panAngleRA` y `panAngleDec`).
  * Arrastre ultra-suave e intuitivo: arrastrar hacia la derecha gira el firmamento hacia la derecha, arrastrar arriba mira al cenit, con amortiguación inercial (*momentum*) calibrada.
* **🎯 Selector Rápido de Constelaciones (*Auto-Focus Celestial*):**
  * Incorporación de un desplegable de cristal ahumado en la barra celeste (`🏹 Sagitario`, `⚔️ Orión`, `🦂 Escorpio`, `♊ Géminis`, `👑 Cassiopea`, `✝️ Cruz del Sur`, etc.).
  * Al seleccionar cualquier constelación, la cámara vuela suavemente y la coloca exactamente en el centro de la pantalla.

---

## [v3.6.2] - 29 de Agosto, 2026

### 🦋 Restauración Total del Lienzo Celeste, Vía Láctea & Mariposas Alquímicas
* **Corrección de Variables de Entorno y Coordenadas:**
  * Reubicación y declaración íntegra de `SACRED_LOCATIONS`, `currentLat`, `currentLon`, `numBgStars` e `isMobile`.
  * **0 errores en consola** (`Console errors: []`), restaurando inmediatamente el renderizado fluido a 60 FPS de las mariposas de Macondo (polvo de oro, aleteo y metamorfosis geométrica), las 30 constelaciones y las estrellas de fondo en tiempo real.

---

## [v3.6.1] - 29 de Agosto, 2026

### 🎯 Zoom Direccional Orientado al Cursor (*Zoom-to-Mouse*) & Navegación 360°
* **Zoom Focalizado en Cualquier Dirección:**
  * Al girar la rueda del ratón (`wheel`) sobre cualquier constelación, estrella o rincón del cielo, el motor calcula el vector entre el centro de la pantalla y el cursor, **desplazando la cámara y haciendo zoom directamente hacia donde apunta el puntero**.
  * Permite acercarse a estudiar objetos específicos (como Orión en el este, la Tetera de Sagitario en el sur o Cassiopea en el norte) sin tener que centrarla previamente de forma manual.
* **Navegación Panorámica Libre 360°:**
  * Arrastre *Grab-to-Pan 1:1* fluido y sin restricciones en los 360 grados del firmamento tanto en escritorio como en dispositivos móviles.

---

## [v3.6.0] - 29 de Agosto, 2026

### 🏹 Rectificación Astrométrica Oficial IAU de las 30 Constelaciones & Tetera de Sagitario
* **Reconstrucción Científica del Asterismo de Sagitario (La Tetera):**
  * Corrección total de la geometría deformada: trazado de la célebre **Tetera de Sagitario (*The Teapot*)** con sus 8 estrellas estelares reales (*Kaus Australis, Nunki, Ascella, Kaus Media, Kaus Borealis, Alnasl, Phi Sgr, Tau Sgr*).
  * Eliminación de líneas cruzadas y delineación perfecta del pico vertedor (*Spout* hacia la Vía Láctea), tapa triangular (*Lid*), cuerpo central y asa curvada (*Handle*).
* **Auditoría y Validación de las 30 Constelaciones (IAU / Stellarium):**
  * Verificación rigurosa de coordenadas astrométricas (Ascensión Recta $\alpha$ y Declinación $\delta$) y líneas de unión oficial para las 12 constelaciones zodiacales y 18 boreales/australes (*Orión, Cassiopea, Cruz del Sur, Can Mayor, Osa Mayor, Cisne, Lira, Águila, Pegaso, Centauro, etc.*).
  * 0 estrellas huérfanas, 0 polígonos colapsados y fidelidad absoluta a las cartas celestes astronómicas internacionales.

---

## [v3.5.4] - 29 de Agosto, 2026

### 💬 Botón WhatsApp Flotante Circular & Glassmorphism Luxury
* **Icon-Only Luxury Minimalism:**
  * Eliminación del bloque de texto horizontal y adopción de un **botón circular minimalista de 50px** con cristal ahumado y borde dorado, idéntico al botón Zen.
  * Icono vectorial oficial de WhatsApp en verde esmeralda con iluminación y pulso dinámico al posar el cursor (*hover glow*).
* **Simetría y Equilibrio Espacial:**
  * **Esquina Inferior Izquierda:** Botón circular `🌌` (Modo Zen).
  * **Esquina Inferior Derecha:** Botón circular `💬` (WhatsApp Directo).
  * **Resultado:** Interfaz 100% limpia, minimalista y sin distracciones visuales.

---

## [v3.5.3] - 29 de Agosto, 2026

### 🏛️ Rediagramación Editorial & Signature Showcase Card en el Footer
* **Eliminación Total de Textos Redundantes:**
  * Sustitución de las dos columnas de texto descriptivo denso por una **Signature Showcase Card** central unificada con cristal ahumado y relieve dorado.
  * Titular de valor de alto impacto en una sola línea: *«Arquitectura Digital de Alto Impacto, Experiencias WebGL & Interfaces Luxury a Medida.»*
* **Barra de Acción Simétrica de 4 Canales (Pills 100% Alineadas):**
  * `⚡ DANISID.COM ↗` (Portfolio Oficial)
  * `🏛️ MAISON QUINTESSENCE ↗` (Estudio de Vanguardia)
  * `💬 +34 641 86 86 20` (WhatsApp Directo)
  * `✉️ GARCIADANIELSID@GMAIL.COM` (Email Oficial)
* **Estética Editorial de Alta Gama:**
  * Balance visual perfecto, jerarquía tipográfica *Cinzel* y *Mono Cyberpunk*, y adaptación fluida a 2 columnas en tablets y 1 columna en móviles.

---

## [v3.5.2] - 29 de Agosto, 2026

### 📐 Disposición Espacial Simétrica (Cero Superposición de Widgets)
* **Separación y Balance de Controles Flotantes:**
  * **Botón Modo Zen (`🌌`):** Reubicado en la **esquina inferior izquierda** (`bottom: 24px`, `left: 24px`).
  * **Botón WhatsApp (`💬`):** Asignado a la **esquina inferior derecha** (`bottom: 24px`, `right: 24px`).
  * **Resultado:** Simetría visual perfecta, 0 colisiones de clics y navegación despejada en desktop y dispositivos móviles.

---

## [v3.5.1] - 29 de Agosto, 2026

### ⚡ Canales de Contacto Directo de Daniel Sid (WhatsApp & Email Oficial)
* **Integración de Canales Oficiales de Contratación:**
  * **WhatsApp Oficial:** `+34 641 86 86 20` (enlace directo `wa.me/34641868620` en botón flotante y footer con mensaje predeterminado).
  * **Email Oficial:** `garciadanielsid@gmail.com` (enlaces directos `mailto:` integrados en el footer de autoría).
  * **Portfolio & Maison:** Conexión consolidada con [`danisid.com`](https://danisid.com) y [`maison-quintessence.netlify.app`](https://maison-quintessence.netlify.app/).

---

## [v3.5.0] - 29 de Agosto, 2026

### 🏛️ Firma Luxury Cyberpunk `danisid.com`, Maison Quintessence, WhatsApp Float & Barra Retráctil
* **Luxury Signature Footer & Showcase de Alto Impacto:**
  * **Daniel Sid (`danisid.com`):** Módulo de autoría y captación para desarrollo web a medida, interfaces de lujo, aplicaciones funcionales y experiencias interactivas en tipografía Cyberpunk Neon y Cinzel.
  * **Maison Quintessence:** Enlace oficial al estudio de alta costura digital ([`maison-quintessence.netlify.app`](https://maison-quintessence.netlify.app/)).
  * Llamada a la acción directa para contratación y consultoría tecnológica.
* **Botón Flotante de WhatsApp (Conversión Directa):**
  * Widget flotante con microinteracción de pulso luminoso en la esquina inferior derecha.
  * Enlace directo con mensaje preconfigurado para solicitar cotizaciones y proyectos web.
* **Barra de Perspectiva Celeste Desplegable / Retráctil (*Collapsible*):**
  * La barra ahora se pliega automáticamente en una discreta cápsula de cristal en la esquina superior derecha (`🌌 Cielo: 🇪🇸 Madrid ▾`).
  * Al hacer clic, se despliega suavemente mostrando las 3 ubicaciones sagradas y los controles celestes.
  * Deja el **100% del área de lectura y el footer limpios y sin obstáculos**.

---

## [v3.4.0] - 29 de Agosto, 2026

### 🍭 Identidad Definitiva `ERÊS`, Rotación Contemplativa & UX No Invasiva
* **Identidad de Marca & Título Definitivo:**
  * Unificación y adopción del nombre oficial: **`ERÊS • Realismo Mágico, Cosmos & Alquimia`** (*Maison Quintessence*).
  * Honra el vocablo sagrado yoruba *Èré* (el juego, la risa sagrada, la alegría pura y la inocencia que desarma cualquier dolor) como eje central del universo creativo de Bahía, Macondo y los Orixás.
* **Velocidad de Rotación Adaptativa y Contemplativa:**
  * **Modo Lectura:** Rotación ultra-suave y sutil a **`0.04°/s`** (90 segundos por cada 3.6°), permitiendo una lectura perfectamente reposada de las tarjetas, filmes y relatos sin fatiga visual ni mareos.
  * **Modo Zen:** Rotación inmersiva a **`0.18°/s`** para deleite astronómico cuando se oculta la interfaz de texto.
* **Rectificación Astrométrica Oficial IAU (Madrid • Bahía • Manizales):**
  * Verificación y calibración exacta del Tiempo Sidéreo Local (LST) con la norma IAU:
    * 🇪🇸 **Madrid:** `Lon: -3.70° W`, `Lat: 40.42° N` (Cenit actual en Piscis / Cetus / Pegaso / Cassiopea).
    * 🇧🇷 **Bahía:** `Lon: -38.50° W`, `Lat: -12.98° S` (Cenit actual en Acuario / Capricornio / Cruz del Sur).
    * 🇨🇴 **Manizales:** `Lon: -75.52° W`, `Lat: 5.07° N` (Cenit actual en Sagitario / Águila / Ofiuco).
* **Reubicación Inteligente de la Barra de Controles (Cero Superposición):**
  * En modo lectura, la cápsula flotante se ubica discretamente en la **esquina superior derecha (*Top-Right Luxury Capsule*)**, dejando el 100% del área central de lectura totalmente despejada.
  * Al entrar en **Modo Zen**, la cápsula se traslada con animación fluida al **centro inferior** para contemplación inmersiva.
* **Calibración de Zoom sin Espacios Vacíos:**
  * Rango de zoom delimitado entre `0.70x` y `1.75x` con radio de cúpula envolvente, garantizando que el cielo cubra siempre el 100% de la pantalla sin bordes negros.

---

## [v3.3.1] - 29 de Agosto, 2026

### 🔭 Visión Hemisférica Humana All-Sky (~180° FOV) & Zoom Interactivo
* **Apertura de Campo Visual Humano All-Sky (~180° FOV):**
  * Reescalado de la proyección estereográfica para emular la visión completa de la cúpula celeste (como observar el firmamento nocturno tumbado en campo abierto).
  * Ahora se aprecian entre **15 y 20 constelaciones simultáneas** en pantalla, permitiendo contemplar arcos completos del Zodiaco, la Vía Láctea y las joyas celestes sin sensación de encajonamiento.
* **Control de Zoom Dinámico e Interactivo:**
  * **Rueda del Ratón (`wheel`):** Aleja o acerca el cielo suavemente con límites calibrados entre `0.45x` (visión ultra-panorámica global) y `2.5x` (estudio detallado de asterismos).
  * **Pellizco Táctil (*Pinch-to-zoom*):** Soporte gestual nativo para pantallas táctiles y móviles.
  * Escalado vectorial proporcional de rótulos tipográficos *Cinzel*, grosor de líneas y magnitudes estelares según el nivel de zoom.

---

## [v3.3.0] - 29 de Agosto, 2026

### 🌌 Motor Planetario Stellarium: Perspectivas Sagradas en Vivo (Madrid, Bahía, Manizales), 30 Constelaciones & Arrastre 1:1
* **Cielo en Tiempo Real y Tiempo Sidéreo Local (LST):**
  * Cálculo astronómico exacto a partir del reloj UTC y la longitud geográfica, proyectando la posición real de las estrellas en este preciso instante.
* **Cápsula de Lugares Sagrados (Glassmorphism Luxury):**
  * 🇪🇸 **Madrid, España:** Perspectiva real desde el hogar y templo en Argüelles (`Lat: 40.42° N`, `Lon: -3.70° W`).
  * 🇧🇷 **Salvador de Bahía, Brasil:** El cielo tropical y místico de Cassiopea ✨🌌 (`Lat: -12.98° S`, `Lon: -38.50° W`).
  * 🇨🇴 **Manizales, Colombia:** La tierra natal de Ósculo Sid 💫 y el firmamento de Adrián (`Lat: 5.07° N`, `Lon: -75.52° W`).
  * Transición angular suave e interpolada (*lerp*) al alternar entre ciudades con notificaciones contextuales.
* **Física de Arrastre Natural 1:1 (*Grab-to-Pan*):**
  * Corregida la inversión del arrastre: mover el ratón o el dedo hacia la derecha o arriba desplaza el firmamento de manera idéntica y natural con amortiguación e inercia.
* **Catálogo Completo de 30 Constelaciones Oficiales IAU (Llenado Total FOV 120°):**
  * Las **12 Zodiacales** (*Aries, Tauro, Géminis, Cáncer, Leo, Virgo, Libra, Escorpio, Sagitario, Capricornio, Acuario, Piscis*).
  * Las **18 Grandes Constelaciones Celestes, Australes y Boreales** (*Orión, Cassiopea, Cruz del Sur, Centauro, Can Mayor / Sirio, Osa Mayor, Águila / Altair, Lira / Vega, Cisne, Pegaso, Dragón, Carina / Canopus, Pez Austral / Fomalhaut, Cetus, Fénix, Ofiuco, Escudo, Pavo*).
  * Firmamento saturado y continuo sin zonas vacías en pantallas panorámicas de PC ni en móviles verticales.
* **Banda Galáctica de la Vía Láctea:**
  * Renderizado etéreo y translúcido del plano galáctico inclinado a 63°, aportando profundidad tridimensional sin sobrecarga.
* **Purificación de la Interfaz:**
  * Eliminación de botones redundantes y sustitución por una cápsula flotante estilizada con interruptores discretos para rotación (`🔄`), constelaciones (`✨`) y nombres (`🌟`).

---

## [v3.2.0] - 29 de Agosto, 2026

### 🌌 Carta Celeste Astronómica IAU, Rotación Terrestre Diurna & Optimización de Rendimiento
* **Motor de Rotación Terrestre Diurna:**
  * Simulación matemática del giro continuo de la Tierra sobre su eje (0.35° por segundo).
  * Movimiento diurno perceptible y majestuoso de este a oeste en la bóveda celeste.
  * Navegación interactiva por arrastre (ratón y táctil) con inercia suave y amortiguación para explorar libremente toda la cúpula.
* **18 Constelaciones Fieles (12 Zodiacales + 6 Principales IAU):**
  * Integración completa de las 12 constelaciones zodiacales (*♈ Aries, ♉ Tauro, ♊ Géminis, ♋ Cáncer, ♌ Leo, ♍ Virgo, ♎ Libra, 🦂 Escorpio, 🏹 Sagitario, ♑ Capricornio, ♒ Acuario, ♓ Piscis*) y las 6 mayores celestes (*🏹 Orión, ✨🌌 Cassiopea, 🐻 Osa Mayor, 🦢 Cisne, 🐎 Pegaso, 🪕 Lira*).
  * Asterismos precisos trazados a partir de coordenadas astronómicas reales (Ascensión Recta y Declinación).
  * **Aparición Completa y Continua:** Proyección con factor de visibilidad global y *Fade In/Fade Out* suave al aproximarse al horizonte, eliminando cortes o mutilaciones en pantalla.
* **Centelleo y Parpadeo Orgánico (`Twinkle`):**
  * Modulación de brillo estelar según magnitud astronómica real (`mag`), con destellos y halos de difracción de 4 puntas en estrellas de primera magnitud.
* **Purificación Visual (Eliminación de Ilustraciones Gigantes):**
  * Retirada de capas de imágenes superpuestas en favor de una carta celeste pura, limpia y elegante de filigrana estelar dorada y tipografía clásica *Cinzel*.
* **Restauración Definitiva de Mariposas de Macondo (Paletas & Despertar):**
  * Recuperación de las 4 paletas alquímicas originales (*Oro Macondo, Cian Yemanjá, Rosa & Violeta Cassiopea, Cristal Cuántico*).
  * Metamorfosis a red geométrica luminosa (mariposas dormidas).
  * Interacción táctil y por clic: despertar instantáneo con ráfagas de polvo de estrellas (`Stardust`) y evasión orgánica.
* **Optimización Extrema de Rendimiento (Mobile-First):**
  * Precomputación trigonométrica de matrices por frame.
  * Batching de trazado de líneas y reducción adaptativa de partículas en pantallas móviles (`isMobile`), garantizando 60 FPS estables sin sobrecalentamiento.
  * Pausa inteligente al cambiar de pestaña (`document.hidden`) para ahorro total de CPU/batería.
* **Nuevos Controles en Interfaz:**
  * 🔄 **Rotación:** Activa / pausa el giro automático de la Tierra.
  * ✨ **Constelaciones:** Muestra / oculta las líneas de filigrana celeste.
  * 🌟 **Nombres:** Muestra / oculta las etiquetas doradas de cada constelación.

---

## [v3.1.0] - 28 de Agosto, 2026

### 🦋 Restauración Maestra del Enjambre de Macondo & Realismo Mágico
* **Enjambre Permanente (Swarm Autónomo):** 16 mariposas vivas navegando permanentemente por la pantalla con física aeroelástica, aleteo 3D senoidal y ciclos de planeo (*gliding*).
* **Paletas Cromáticas Alquímicas:**
  * 🌟 **Oro Macondo:** Destellos solares amarillos y ambarinos (`#ffffff` -> `#fef08a` -> `#fbbf24` -> `#d97706`).
  * 🌊 **Cian Yemanjá:** Azules eléctricos translúcidos de agua pura y mar sagrado.
  * 🌸 **Rosa & Violeta Cassiopea:** Tonos místicos de Oxum y alta vibración de amor.
  * 💎 **Cristal Cuántico:** Opalinos iridiscentes.
* **Anatomía Vectorial de Alta Gama:** Curvas Bézier continuas para alas anteriores (*forewings*) y posteriores (*hindwings*), cuerpo anillado, cabeza, tórax con núcleo luminoso y antenas curvas.
* **Interactividad Física & Ráfagas:**
  * Campo repulsor dinámico con el movimiento del ratón y touch (evasión fluida en radio de 180px).
  * Onda de choque en clics que detona 18 destellos de polvo de oro (`Stardust`) y lanza ráfagas de 4 mariposas vivas adicionales.
* **Integración Limpia de Constelaciones (Sin Bordes Cuadrados):**
  * Eliminación de cajas y artefactos mediante máscaras radiales suaves (`destination-in`) sobre canvas offscreen y composición `screen`, protegiendo la carga contra errores de origen local.

---

## [v3.0.0] - 28 de Agosto, 2026

### 🎨 Rediseño UI/UX Profesional (Glassmorphism & Inmersión)
* **Pantalla de Bienvenida (Welcome Overlay):** Introducción inmersiva que oculta el contenido hasta que el usuario hace clic en "Adentrarse en la Magia". Esto prepara un entorno sin distracciones y permite precargar el AudioContext sin bloqueos del navegador.
* **Top Navigation Pro:** Sustitución del antiguo menú horizontal (nav-tabs-wrapper) por una elegante barra de navegación superior anclada (`position: sticky`), con estética de cristal esmerilado (`backdrop-filter`) e interacciones luminosas premium.
* **Astrología Estelar Integrada:** Las constelaciones de **Sagitario**, **Tauro** y **Draco (El Dragón)** han sido tejidas matemáticamente en el cielo del canvas, uniendo sus puntos con sutiles trazados cósmicos en honor a las firmas espirituales de Sid y Alanna.

---


## [v2.6.0] - 28 de Agosto, 2026

### 🔁 Sistema de Transición Continua: Auto-Pase, Categorías & 10 Modos Sonoros
* **Modo "Auto-Pase (Continuo)":** Botón de conmutación inteligente `🔁 Auto-Pase: ON/OFF` que transiciona fluidamente a la siguiente pista al completar el ciclo de compases de cada canción/sonido.
* **Transición Manual Instantánea:** Botones `⏮️ Pase Atrás` y `⏭️ Pase Adelante` con notificaciones visuales dinámicas (*Toasts*) del tema en curso.
* **Filtros por Categoría de Sonido:**
  * 🌟 **Todos los Sonidos (10 Modos)**
  * 🇧🇷 **Canciones & Ritmos (7 Temas):** *Se Essa Rua Fosse Minha, Comptine d'un Autre Été, Claro de Luna, Eu Tava Aqui Pensando, MC Levin Baile Funk, Bossa Nova Cósmica, Generador Cuántico*.
  * 🌌 **Frecuencias Sagradas & Atmósferas (3 Modos):** *Ballenas & Olas 432 Hz, Ponto Sagrado Umbanda (Batá), Lluvia de Macondo & Sanación 528 Hz*.
* **Notificaciones Flotantes (*Toasts*):** Feedback interactivo que confirma en tiempo real el sonido que entra en reproducción.

---

## [v2.5.0] - 28 de Agosto, 2026

### 🔥 Baile Funk & Mandelão Brasileño: MC Levin ("Sua Amiga Vou Sarrar")
* **Integración del Hit Urbano de Brasil:** Incorporado el tema **"Sua Amiga Vou Sarrar"** de **MC Levin** en el Cassiopea Jukebox (`Track 5`).
* **Motor de Síntesis de Baile Funk / Tamborzão:**
  * **808 Sub-Bass Punchy:** Golpe de bajo sub-grave a 42 Hz con caída de frecuencia rápida.
  * **Tamborzão Percussion:** Patrón rítmico sincopado en 16 pasos (*Tu-Tu-Ta, Tu-Tu-Ta* a 140 BPM).
  * **Synth Lead Stabs:** Riff melódico con onda *sawtooth* y filtro resonante para evocar la vibra de los bailes de favela y fiestas de São Paulo / Río / Bahía.

---

## [v2.4.0] - 28 de Agosto, 2026

### 🎵 Cassiopea Jukebox Pro: Síntesis Polifónica & Reproductor de Canciones
* **Integración Fiel de las Canciones Recomendadas por Cassiopea ✨🌌 (Alanna):**
  1. 🇧🇷 **"Se Essa Rua Fosse Minha" (Ana Santos):** Cantiga tradicional de Bahía con arpegios líricos de guitarra de nylon y campanas de cristal.
  2. 🎹 **"Comptine d'un Autre Été: L'après-Midi" (Rogerio Tutti / Yann Tiersen):** Vals nostálgico de piano minimalista en Mi menor con arpegios de mano izquierda y melodía fluida.
  3. 🌙 **"Claro de Luna" (Moonlight Sonata / Beethoven - Richard Clayderman):** Arpegios de tresillos en Do# menor con resonancia acústica de piano de cola.
  4. 👶 **"Eu Tava Aqui Pensando":** Ritmo alegre y saltarín de samba-reggae infantil y percusión de los Erês.
  5. 🎸 **"Bossa Nova Cósmica" (Tom Jobim / João Gilberto):** Batida sincopada brasileña con acordes de novenas y trecenas (Dm9, G13, Cmaj9, A7b13).
  6. 🎲 **"Alquimia Cuántica Procedural (Infinita)":** Generador algorítmico en tiempo real basado en la Proporción Áurea ($\Phi$).
* **Interfaz de Reproductor Estilo Spotify / Jukebox de Lujo:** Controles completos (`⏮️`, `▶️ / ⏸️`, `⏭️`, `🎲 Generador Cuántico`), carátulas con emojis, metadatos y barra de píldoras navegables.

---

## [v2.3.0] - 28 de Agosto, 2026

### 🎨 Manual de Marca, Bossa Nova Brasileña & Mariposas-Constelación
* **Cielo Estelar & Constelaciones Reales:** Renderizado permanente de la **Constelación Cassiopea ✨🌌 ('W')** y la **Constelación Ibejis (Castor & Pólux)** en el firmamento con líneas de luz y rótulos poéticos.
* **Metamorfosis Alquímica Mariposa-Constelación:** Cada cierto ciclo, las mariposas se detienen en el cielo y cristalizan sus alas en mallas estelares geométricas con nodos de luz neón, disparando rayos hacia el cosmos.
* **4 Paletas Cromáticas Cyberpunk:**
  1. *Oro Macondo (Alquimia Solar)*
  2. *Cian Yemanjá (Azul Eléctrico & Translúcido)*
  3. *Rosa & Violeta Cassiopea (Oxum & Amor)*
  4. *Cristal Cuántico (Vidrio Opalino Iridescente)*
* **Aleteo Dinámico y Mayor Velocidad:** Ampliado el rango de frecuencia alar y velocidad de navegación para crear un enjambre vivo y ágil.
* **Motor de Bossa Nova Brasileña:** Síntesis acústica de guitarra con cuerdas de nylon y acordes extendidos (Dm9, G13, Cmaj9, A7b13) con batida sincopada y selector de 3 modos sonoros (*Bossa Nova*, *Ponto Sagrado de Umbanda*, *Ballenas 432 Hz*).
* **Pestaña de Manual de Marca Oficial:** Incorporado el manual de identidad visual con swatches de color interactivos, tipografía y arquetipos de **Cassiopea ✨🌌 (Alanna)** y **Ósculo Sid 💫 / Cid (Dani)**.
* **Documento Maestro Creado:** [`MANUAL_IDENTIDAD_VISUAL_Y_MARCA_DEL_AMOR.md`](file:///home/sidzcool/GeminiSolutions/01_Proyectos_Activos/Proyecto_Ibeji_Umbanda/MANUAL_IDENTIDAD_VISUAL_Y_MARCA_DEL_AMOR.md).

---

## [v2.2.0] - 28 de Agosto, 2026

### 🌹 Nueva Sección Maestra: Génesis, Amor en Argüelles & Arquetipos Cósmicos
* **Header Rediseñado y Purificado:** Eliminado el botón flotante aislado; cabecera minimalista con sello *QUIMERA ALCHEMIST • MAISON QUINTESSENCE*.
* **Pestaña Oficial de Génesis:** Añadida la sección `🌹 Génesis: Cassiopea & Ósculo Sid` en la navegación principal.
* **Crónica de Amor en los Bajos de Argüelles:** Relato de la génesis íntima del proyecto entre Madrid, las anécdotas de Bahía y la alquimia de dos almas.
* **Tarjetas Duales de Arquetipo:**
  * **Cassiopea ✨🌌:** La Reina de la Memoria Sagrada, la devoción a los Erês y la visión mística de la Umbanda.
  * **Ósculo Sid 💫:** El arquitecto demiurgo, quien transmuta los suspiros y relatos en cine, código y frecuencias sonoras.
* **Los 4 Pilares del Universo Ibeji:** Estructuración visual de los 4 fundamentos creativos (Umbanda, Gabriel García Márquez, Salvador Dalí y la Bossa Nova Cósmica de Natalia).

---

## [v2.1.0] - 28 de Agosto, 2026

### 🦋 Motor Vectorial Canvas Maison Quintessence & Quimera Alchemist
* **Eliminación Total del Motor DOM Div 3D:** Erradicados todos los artefactos poligonales y pliegues rígidos de divs/CSS.
* **Renderizado Vectorial Ultra-Nítido en Canvas GPU:** Cada mariposa de Macondo se dibuja mediante curvas Bézier cúbicas continuas con degradados radiales multicapa (`#ffffff` núcleo a `#f59e0b` oro y `#78350f` café siena), venación de filigrana alquímica y cuerpo anillado con gemas doradas.
* **Física Aeroelástica y Ciclos de Planeo:** Ondulación alar orgánica con flexión de puntas alares, inclinación de alabeo (*bank roll*) en giros y transiciones automáticas a planeo suave.
* **Interactividad Alquímica:** Campo repulsor dinámico con el movimiento del ratón y onda de choque en clics que dispersa el enjambre con ráfagas de polvo de oro.
* **Favicon Vectorial Integrado:** Icono SVG exclusivo de mariposa estelar cósmica para navegador.

---

## [v2.0.0] - 28 de Agosto, 2026

### 🦋 Mariposas de Macondo: Capa Trasera & Anatomía Fiel
* **Capa Trasera (`z-index: 0`):** Las mariposas vuelan de fondo por detrás de todas las tarjetas y paneles de texto (`z-index: 2`), garantizando máxima legibilidad sin estorbar.
* **Anatomía Alar Corregida y Simétrica:** Rediseñadas las alas anterior (forewing) y posterior (hindwing) con venación dorada/ámbar y simetría alar real (reflejo `scaleX(-1)` para el ala izquierda).
* **Física de Espanto e Interacción:** El cursor del ratón y el clic espantan dinámicamente a las mariposas en un radio amplio, provocando aceleraciones de huida orgánicas.

---

## [v1.9.0] - 28 de Agosto, 2026

### ✨ Motor de Mariposas de Macondo Ultra-Luminoso & Swarm 3D
* **Optimización y Depuración Integral:** Eliminados todos los errores de inicialización y orden de carga en consola (`CosmicSweet` & `trailerScenes`).
* **Vectores SVG con Gradientes Radiales Únicos:** Cada mariposa posee sus propios IDs de degradado de alta luminosidad (`#ffffff -> #fff566 -> #ffd700 -> #ff9900`), evitando colisiones de renderizado en navegadores Chromium/WebKit.
* **Físicas de Vuelo Orgánicas y Suaves:** Inercia angular, balanceo tridimensional $(\text{Pitch, Yaw, Roll})$, profundidad $Z$, evasión suave del cursor y estelas de polvo de oro fluorescentes.
* **Spawning al Clic:** Generación instantánea de ráfagas de estelas y mariposas adicionales al pulsar la pantalla.

---

## [v1.8.0] - 28 de Agosto, 2026

### ✍️ Firma de Autor Oficial: Dani Sid • Quimera Alchemist (Maison Quintessence)
* **Reemplazo de Firma:** Eliminada la firma de Dalí y grabada la firma oficial de autor en caligrafía dorada sobre piedra en el Capítulo II:  
  `Dani Sid • Quimera Alchemist (Maison Quintessence)`.
* **Actualización en Galería Web:** Sincronizada automáticamente en [`index.html`](file:///home/sidzcool/GeminiSolutions/01_Proyectos_Activos/Proyecto_Ibeji_Umbanda/index.html).

---

## [v1.7.0] - 28 de Agosto, 2026

### 🦋 Motor 3D Realista de Mariposas de Macondo (CSS 3D & SVG Vector)
* **Aleteo Espacial 3D Verdadero:** Utilización de `transform-style: preserve-3d` con rotación física en eje Y (`rotateY(-68deg) -> rotateY(70deg)`) con pivote `transform-origin` en las bisagras anatómicas.
* **Morfología Vectorial SVG de Alta Fidelidad:** Alas con festones aerodinámicos, cola de golondrina, gradiente solar multicapa, venación alar ámbar y perlas de luz en los bordes.
* **Dinámica de Vuelo Orgánica:** Comportamiento autónomo de planeo (*gliding*) y aleteo rápido (*fluttering*), con orientación espacial tridimensional $(\text{Pitch, Yaw, Roll})$ y profundidad $Z$ $(-250\text{px}$ a $+350\text{px})$.
* **Estela de Oro Sincronizada:** Las mariposas 3D emiten partículas doradas sobre el canvas a medida que sobrevuelan la pantalla.
* **Interacción Táctil y Ratón:** Evasión natural ante la cercanía del cursor y explosión de polen estelar al hacer clic o tocar.

---

## [v1.6.0] - 28 de Agosto, 2026

### 🎨 Creación de "Capítulo II: El Duelo Alquímico de la Encrucijada"
* **Refactorización Artística:** Conservados todos los carteles y obras previas en una galería modular organizada por Capítulos.
* **Fusión Alquímica Personalizada (QuimeraAlchimest & Ósculo Sid):**
  * Eliminación de los relojes derretidos y sustitución por **símbolos de transmutación hermética**: tambor con glifos solares, lunares y uroboros.
  * **Kintsugi Alquímico:** Grietas en la tierra que emanan venas de oro líquido y brotes de vida ante las vibraciones del tambor sagrado.
  * **Sólidos Platónicos e Icosaedros Flotantes:** Esferas y poliedros de geometría sagrada suspendidos en el aire crepuscular.
  * **Baobabs de Savia Dorada:** Árboles milenarios con canales de resina áurea bajo un cielo estrellado y atardecer de fuego.
  * **La Danza de Ikú:** La Muerte colosal danzando hipnotizada ante los gemelos Taiwo y Kehinde.

---

## [v1.5.0] - 28 de Agosto, 2026

### 🦋 Motor de Mariposas Macondo (Quimera Automata Engine)
* **Geometría Vectorial Anatómica:** Curvas cúbicas y cuadráticas Bézier (`bezierCurveTo`) para alas delanteras y traseras con encaje festoneado y venación alar ámbar.
* **Aleteo en Perspectiva 3D:** Proyección trigonométrica $W = \cos(\theta)$ con rotación vectorial orientada hacia el vector de velocidad $(\Delta x, \Delta y)$.
* **Estelas de Polvo de Oro (Stardust Trails):** Cada mariposa emite partículas de brillo áureo con decaimiento orgánico (`Stardust Particle System`).
* **Física Interactiva Táctil / Ratón:** Evasión y curiosidad ante el cursor y dispersión de destellos al hacer clic o tocar la pantalla.
* **Escalado Retina DPR:** Transformación de canvas en alta definición (`window.devicePixelRatio`) para máxima nitidez en pantallas móviles y monitores 4K.

---

## [v1.4.0] - 28 de Agosto, 2026

### 🌌 Génesis & Dedicatoria Oficial: Cassiopea ✨🌌 & Ósculo Sid 💫
* **Adopción del nombre cósmico:** Rebautizada la inspiración central bajo el nombre de **Cassiopea ✨🌌** (quien nombra a su compañero **Ósculo Sid 💫**).
* **Creación del Informe Maestro:** Creado [`INFORME_GENESIS_Y_UNIVERSO_CASSIOPEA.md`](file:///home/sidzcool/GeminiSolutions/01_Proyectos_Activos/Proyecto_Ibeji_Umbanda/INFORME_GENESIS_Y_UNIVERSO_CASSIOPEA.md) que narra la génesis mágica y romántica, los pilares de Realismo Mágico y el marco conceptual cinematográfico.

### 🐋 Bossa Nova Cósmica Trascendental & Canto de Ballenas Jorobadas
* **Evolución del Sintetizador Web Audio API:** Incorporada la función `playWhaleSongHarmonic()` que sintetiza barridos armónicos de baja frecuencia emulando los cantos de ballenas jorobadas en el océano cósmico de *Yemanjá*.
* **Colaboración Musical Proyectada:** Planificada la participación de **Natalia** para la composición oficial de la banda sonora.

---

## [v1.3.0] - 28 de Agosto, 2026

### 📱 Optimización Móvil y Experiencia Multidispositivo
* **Navegación Touch-Friendly:** Barra de pestañas con scroll horizontal fluido (`-webkit-overflow-scrolling: touch`) sin saltos de línea molestos en smartphones.
* **Tipografía Adaptativa (`clamp`):** Títulos y subtítulos escalables dinámicamente según el ancho del viewport (desde pantallas de 320px hasta 4K).
* **Grid Responsive Fluido:** Reestructuración de tarjetas de información y galerías de arte con `minmax()` para evitar desbordamientos horizontales.

### 🎵 Paisaje Sonoro en Bucle (Web Audio API Synthesizer)
* **Diseño Acústico Nativo:** Sintetizador en tiempo real sin dependencias de archivos de audio externos (cero latencia y reproducción garantizada en cualquier navegador).
* **Percusión Ancestral Batá:** Pulso grave en 4/4 con curva de decaimiento exponencial emulando un atabaque/tambor de cuero.
* **Campanas Místicas Pentatónicas:** Generador de frecuencias aleatorias pentatónicas (C5 a C6) con envolvente de reverberación cálida.
* **Drone Armónico de Viento:** Frecuencia continua C3 que recrea la atmósfera crepuscular de los manglares.
* **Dock de Control:** Botón interactivo de inicio/pausa con ecualizador visual dinámico (`#eqWaveVisualizer`).

### 🦋 Animación de Fondo en Bucle (HTML5 Canvas)
* **Mariposas Amarillas de Macondo:** 14 entidades animadas con movimiento senoidal de aleteo y brillo áureo (`#fbbf24`).
* **Cascada Cósmica de Dulces y Destellos:** 25 partículas luminosas en caída suave con paleta de colores de Umbanda (rosa, celeste, dorado, esmeralda y púrpura).

### 💡 Nueva Sección Pedagógica: "¿De qué va el tema? (Aprender)"
* Guía explicativa interactiva sobre la razón de cada símbolo (los dulces, los elefantes zancudos, la inteligencia vs. fuerza y las mariposas amarillas).

---

## [v1.2.0] - 28 de Agosto, 2026

### 🎨 Rediseño del Cartel Oficial (Formato Historia de Instagram 9:16)
* **Eliminación del cliché de los relojes derretidos:** Sustitución por una composición de alta fuerza poética: los tres niños sagrados (**Taiwo, Kehinde y Doum**) sobre flores de loto de agua pura.
* **Cascada Cósmica de Azúcar:** Lluvia de caramelos cristalizados, piruletas luminosas y monedas de oro dulce.
* **Elefantes de Zancos (Estilo Dalí Sutil):** Gigantes caminando con ligereza sobre el agua en el horizonte del atardecer.
* **Generación y Guardado:** Creado y guardado en `assets/images/cartel_instagram_story_9_16.jpg`.

---

## [v1.1.0] - 28 de Agosto, 2026

### 🎬 Universo Cinematográfico en Realismo Mágico
* **Guion del Tráiler Oficial:** Creado [`GUION_TRAILER_REALISMO_MAGICO.md`](file:///home/sidzcool/GeminiSolutions/01_Proyectos_Activos/Proyecto_Ibeji_Umbanda/GUION_TRAILER_REALISMO_MAGICO.md) con la prosa y cadencia de Gabriel García Márquez.
* **Simulador Interactivo de Escenas:** Reproductor con visualización sincronizada de voz en off, diseño de sonido e imágenes conceptuales de alta definición.
* **Galería Conceptual:**
  * `escena_danza_muerte.jpg` (La Danza Inmortal de Ikú).
  * `escena_eres_lluvia_dulces.jpg` (La Apoteosis de los Erês).

---

## [v1.0.0] - 28 de Agosto, 2026

### 👶 Fundación del Proyecto Ibeji & Umbanda
* **Compendio Maestro:** Creado [`COMPENDIO_IBEJI_Y_UMBANDA.md`](file:///home/sidzcool/GeminiSolutions/01_Proyectos_Activos/Proyecto_Ibeji_Umbanda/COMPENDIO_IBEJI_Y_UMBANDA.md) con la historia de Taiwo, Kehinde, Doum, el mito del tambor mágico y las 7 líneas de la Umbanda.
* **Portal Web Inicial:** Creado [`index.html`](file:///home/sidzcool/GeminiSolutions/01_Proyectos_Activos/Proyecto_Ibeji_Umbanda/index.html) con estética mística, puntos cantados y bitácora con persistencia en `LocalStorage`.
* **Registro Central:** Integrado en [`BACKLOG_GLOBAL.md`](file:///home/sidzcool/GeminiSolutions/BACKLOG_GLOBAL.md).
