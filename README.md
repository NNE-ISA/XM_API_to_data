# XM_API_to_data

El codigo ene ste repositorio permite a descargar información sobre el Sistema electríco Colombiano, por medio de Python utilizando la API de XM, la información esta organizada como se muestra en la siguiente tabla.

<table class="default">
<tr><th>Item</th> <th>Frecuencia</th> <th>Variable</th> <th>Nombre</th></tr>
  
<tr><th rowspan="25">Sistema</th> <td rowspan="12">Horaria</td> <td>Generacion Ideal</td> <td>GeneIdea</td></tr>
<tr><td>Generacion Real                  </td> <td>Gene             </td></tr>
<tr><td>Demanda Comercial                </td> <td>DemaCome         </td></tr>
<tr><td>Precio de Bolsa Nacional         </td> <td>PrecBolsNaci     </td></tr>
<tr><td>Máximo Precio de Oferta Nacional </td> <td>MaxPrecOferNal   </td></tr>
<tr><td>Restricciones Aliviadas          </td> <td>RestAliv         </td></tr>
<tr><td>Ventas en Contratos Energía      </td> <td>VentContEner     </td></tr>
<tr><td>Compras en Contratos Energía     </td> <td>CompContEner     </td></tr>
<tr><td>Compras en Bolsa Nacional Energía</td> <td>CompBolsNaciEner </td></tr>
<tr><td>factor emision CO2e              </td> <td>factorEmisionCO2e</td></tr>
<tr><td>Importaciones Energía            </td> <td>ImpoEner         </td></tr>
<tr><td>Perdidas en Energia              </td> <td>PerdidasEner     </td></tr>

<tr><td rowspan="12">Diaria</td> <td>Aportes Energia</td>  <td>AporEner</td></tr>
<tr><td>Precio de Escasez de Activacion           </td>  <td>PrecEscaAct       </td></tr>
<tr><td>Remuneración Real Ind. Cargo Confiabilidad</td>  <td>RemuRealIndiv     </td></tr>
<tr><td>Precio Promedio Contratos Regulado        </td>  <td>PrecPromContRegu  </td></tr>
<tr><td>Precio Promedio Contratos NO Regulado     </td>  <td>PrecPromContNoRegu</td></tr>
<tr><td>Volumen Util Diario en Energia            </td>  <td>VoluUtilDiarEner  </td></tr>
<tr><td>Demanda del SIN                           </td>  <td>DemaSIN           </td></tr>
<tr><td>Capacidad Util Diaria en Energia          </td>  <td>CapaUtilDiarEner  </td></tr>
<tr><td>Media Historica Aportes                   </td>  <td>AporEnerMediHist  </td></tr>
<tr><td>FAZNI                                     </td>  <td>FAZNI             </td></tr>
<tr><td>PRONE                                     </td>  <td>PRONE             </td></tr>
<tr><td>FAER                                      </td>  <td>FAER              </td></tr>

<tr><td>Anual</td> <td>Listado de recursos térmicos CEN por mes</td> <td>CapEfecNeta</td></tr>


<tr><th rowspan="8">Recursos</th> <td rowspan="7">Horaria</td> <td>Generacion Ideal</td> <td>GeneIdea</td></tr>
<tr><td>Generación Real                               </td> <td>Gene               </td></tr>
<tr><td>Cosumo de combustible Aprox. Factor de Emisión</td> <td>ConsCombustibleMBTU</td></tr>
<tr><td>Precio de Oferta del Despacho                 </td> <td>PrecOferDesp       </td></tr>
<tr><td>Emisiones CO2e                                </td> <td>EmisionesCO2Eq     </td></tr>
<tr><td>Generación Seguridad                          </td> <td>GeneSeguridad      </td></tr>
<tr><td>Generación Fuera de Merito                    </td> <td>GeneFueraMerito    </td></tr>

<tr><td>Diaria</td> <td>Obligaciones de Energía Firme</td> <td>ObligEnerFirme</td></tr>

<tr><th rowspan="4">Recursos Combinados</th> <td rowspan="4">Horaria</td> <td>Consumo Comb Aprox</td> <td>ConsCombAprox</td></tr>
<tr><td>Emisiones CO                              </td> <td>EmisionesCO2    </td></tr>
<tr><td>Emisiones CH                              </td> <td>EmisionesCH4    </td></tr>
<tr><td>Emisiones N2                              </td> <td>EmisionesN2O    </td></tr>

<tr><th rowspan="5">Agentes</th> <td rowspan="5">Horaria</td> <td>Demanda Comercial</td> <td>DemaCome</td></tr>
<tr><td>Ventas en Contratos Energía               </td> <td>VentContEner    </td></tr>
<tr><td>Compras en Contratos Energía              </td> <td>CompContEner    </td></tr>
<tr><td>Compras en Bolsa Nacional Energía         </td> <td>CompBolsNaciEner</td></tr>
<tr><td>Demanda por Operador de Red               </td> <td>DemaOR          </td></tr>       

<tr><th rowspan="2">Rios</th> <td rowspan="2">Diaria</td> <td>Aportes Energia</td> <td>AporEner</td></tr>
<tr><td>Media Historica Aportes                   </td> <td>AporEnerMediHist</td></tr>

<tr><th rowspan="2">Embalses</th> <td rowspan="2">Diaria</td> <td>Volumen Util Diario en Energia</td> <td>VoluUtilDiarEner</td></tr>
<tr><td>Capacidad Util Diaria en Energia</td> <td>CapaUtilDiarEner</td></tr>

<tr><th rowspan="2">Areas</th> <td rowspan="2">Diaria</td> <td>Demanda No Atendida Programada por Área</td> <td>DemaNoAtenProg</td></tr>
<tr><td>Demanda No Atendida No Programada por Área</td> <td>DemaNoAtenNoProg</td></tr>

<tr><th rowspan="2">Subareas</th> <td rowspan="2">Diaria</td> <td>Demanda No Atendida Programada por Subarea</td> <td>DemaNoAtenProg</td></tr>
<tr><td>Demanda No Atendida No Programada por Subarea</td> <td>DemaNoAtenNoProg</td></tr>

</table>



### Que hace este codigo sobre la información extraida de a API
+ Permite descargar información de varias variables a la vez
+ Organiza automaticamente los datos en formato de tabla normalizada, y cruza la información de las dititntas varaibles
+ Obtiene la información con los nombres de los nombres y no solamente con el codigo de sub mercado
+ Organiza la información en el formato correcto; las fechas como fechas, los números como números (originalmente todos son string)

### En que formato se extrae la información
+ En el caso de utilizar la consola pide lso datos uno a uno disminuyendo la posibilidadde consultas erroneas, ademas de guardar automaticamente la información como documento .csv
+ En el caso de utilizarla desde un notebook o un editor de cogido permite trabajar con ella en formato Dataframe


# Como se utiliza
------------------

### Requerimientos previos

~~~
**software**
Python 3.x

**Paquetes**
pandas
datetime
json
request
~~~
#### Intalación
Python se puede instalar de varias formas de instalar python y los paquetes necesarios
+ Desde la web oficial de [Python](https://www.python.org/downloads/)
~~~
pip install pandas
pip install datetime
pip install json
pip install request
~~~
+ Utilizando [Anaconda](https://www.anaconda.com/products/individual) o [miniconda](https://docs.conda.io/en/latest/miniconda.html)
~~~
conda install pandas
conda install datetime
conda install json
conda install request
~~~


#### Obtener el código
Devido a que no es un paquete oficial, para utilizar el código de este repositorio, primero se debe descargar el código como .zip (y descomprimirlo) o clonar el repositorio en la maquina local (En cuyo caso es necesario git).

### Utilizar el codigo
Para utilizar este codigo hay dos caminos, el primero, utilizando la linea de comandos y el segundo utilizando un editor de codigo que soporte Python.

#### Con la linea de comandos
Existen 

