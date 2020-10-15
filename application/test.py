import os

from os import path
from PIL import Image
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords

## make sure i have download 'stopwords', 'punkt' 
nltk.download(['stopwords', 'punkt'])
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

stop_words = set(stopwords.words('spanish'))
# Read the whole text.
text = """ 

En la Segunda Guerra Mundial, las máquinas de cifrado mecánicas y electromecánicas se utilizaban extensamente, aunque —allá donde estas máquinas eran poco prácticas— los sistemas manuales continuaron en uso. Se hicieron grandes avances en la rotura de cifrados, todos en secreto. La información acerca de esta época ha empezado a desclasificarse al llegar a su fin el periodo de secreto británico de 50 años, al abrirse lentamente los archivos estadounidenses y al irse publicando diversas memorias y artículos.

Los alemanes hicieron gran uso de diversas variantes de una máquina de rotores electromecánica llamada Enigma. El matemático Marian Rejewski, de la Oficina de Cifrado polaca, reconstruyó en diciembre de 1932 la máquina Enigma del ejército alemán, utilizando la matemática y la limitada documentación proporcionada por el capitán Gustave Bertrand, de la inteligencia militar francesa. Este fue el mayor avance del criptoanálisis en más de mil años. Rejewsky y sus colegas de la Oficina de Cifrado, Jerzy Różycki y Henryk Zygalski, continuaron desentrañando la Enigma y siguiendo el ritmo de la evolución de los componentes de la máquina y los procedimientos de cifrado. Al irse deteriorando los recursos financieros de Polonia por los cambios introducidos por los alemanes, y al irse avecinando la guerra, la Oficina de Cifrado, bajo órdenes del estado mayor polaco, presentaron a representantes de la inteligencia francesa y británica los secretos del descifrado de la máquina Enigma, el 25 de julio de 1939, en Varsovia.

Poco después de que estallara la Segunda Guerra Mundial el 1 de septiembre de 1939, el personal clave de la Oficina de Cifrado fue evacuado hacia el sureste; el 17 de septiembre, tras la entrada de la Unión Soviética en el este de Polonia, cruzaron Rumanía. Desde allí alcanzaron París, en Francia; en la estación de inteligencia polaco-francesa PC Bruno, cerca de París, continuaron rompiendo la Enigma, colaborando con los criptólogos británicos de Bletchley Park, que se habían puesto al día con el tema. Con el tiempo, los criptólogos británicos —entre los que se incluían nombres como Gordon Welchman y Alan Turing, el fundador conceptual de la computación moderna— hicieron progresar sustancialmente la escala y tecnología del descifrado Enigma.

El 19 de abril de 1945 se ordenó a los oficiales superiores británicos que nunca debían revelar que se había roto el código de la máquina Enigma alemana, porque esto le daría la oportunidad al enemigo de decir que «no fueron vencidos justa y satisfactoriamente».2​

Los criptógrafos de la Armada estadounidense (en cooperación con criptógrafos británicos y holandeses a partir de 1940) rompieron varios sistemas criptográficos de la Armada japonesa. La rotura de uno de ellos, el JN-25, condujo a la célebre victoria estadounidense de la batalla de Midway. Un grupo del ejército estadounidense, el SIS, consiguió romper el sistema criptográfico diplomático japonés de alta seguridad (una máquina electromecánica llamada Púrpura por los estadounidenses) antes incluso del comienzo de la Segunda Guerra Mundial. Los estadounidenses llamaron a la inteligencia derivada del criptoanálisis, quizás en especial la derivada de la máquina Púrpura, como «Magic» (Magia). Finalmente los británicos se decidieron por «Ultra» para la inteligencia derivada del criptoanálisis, en especial la derivada del tráfico de mensajes cifrados con las diversas Enigmas. Un término británico anterior fue para Ultra fue «Boniface».

Los militares alemanes también desarrollaron varios intentos de implementar mecánicamente la libreta de un solo uso. Bletchley Park los llamó cifrados Fish, y Max Newman y sus colegas diseñaron e implementaron el primer ordenador electrónico digital programable del mundo, Colossus, para ayudarles con el criptoanálisis. La Oficina de Asuntos Exteriores alemana empezó a usar la libreta de un solo uso en 1919; parte de este tráfico fue leído en la Segunda Guerra Mundial como resultado de la recuperación de material importante en Sudamérica que fue desechado con poco cuidado por un mensajero alemán.

La Oficina de Asuntos Exteriores japonesa utilizó un sistema eléctrico lógico basado en uniselectores (llamado Púrpura por EE. UU.), y también utilizó varias máquinas similares para los agregados de algunas embajadas japonesas. Una de estas recibió el nombre de «Máquina M» por EE. UU., y otra fue apodada «Red». Todas fueron rotas en mayor o menor grado por los aliados.


SIGABA se describe en la Patente USPTO n.º 6175625, registrada en 1944 pero no publicada hasta 2001.
Las máquinas de cifrado aliadas utilizadas en la Segunda Guerra Mundial incluían la Typex británica y la SIGABA estadounidense; ambos eran diseños de rotores electromecánicos similares en espíritu a la Enigma, aunque con mejoras importantes. No se tiene constancia de que ninguna de ellas fuera rota durante la guerra. Los polacos utilizaron la máquina Lacida, pero se demostró que era poco segura y se canceló su uso. Las tropas de campo utilizaron las familias M-209 y M-94. Los agentes SOE utilizaron inicialmente «cifrados de poema» (las claves eran poemas memorizados), pero más avanzada la guerra empezaron a utilizar libretas de un solo uso.

"""

# Generate a word cloud image
wordcloud = WordCloud(stopwords = stop_words, background_color='white',max_words=100).generate(text)

wordcloud.to_file('wc.png')
# # lower max_font_size
# image = wordcloud.to_image()
# image.show()


