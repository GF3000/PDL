# clase temporal para guardar el codigo de la tabla de simbolos, ya que estaba implementando
# tbn el trabajo del analizador semantico y era mucho mas sencillo

 elif token_type == 'IDENTIFIER': #Si es un identificador, lo añadimos a la tabla de simbolos
                #         Integer idPalRes = this.palabrasReservadas.get(this.stringActual);
				# if (idPalRes != null) {
				# 	return this.generaToken("PAL_RES", idPalRes);
				# } else {
				# 	EntradaTS entrada = this.control.buscarEntradaPorLexema(this.stringActual);

				# 	if (entrada == null) {
				# 		entrada = this.control.insertarEntrada(this.stringActual);
				# 	}
				# 	return this.generaToken("ID", entrada.getId());
				# }
                        # comprobar si esta ya en la TS, si no esta, lo añadimos
                        # el analizador lexico solo introduce los lexemas
                        # print(self.symbol_table.getEntradasTS(value))
                        if (self.symbol_table.getEntradasTS(value) == None):
                            self.symbol_table.addEntrada(value)

                        # ------ todo lo comentado resulta que va a ir en el an. semantico no aqui xd, pero lo dejo para reutilizarlo luego
                        # cogemos el ultimo token si hay
                        # lastToken = self.get_last_token()

                        # if (lastToken != None) and (self.get_last_token().get_type() == 'PalRes'):
                            
                        #     token_atrib = self.get_last_token().atr()
                        #     if token_atrib == 'function':
                        #         self.symbol_table.addEntrada(value)
                        #         # self.symbol_table.addEntrada(value, self.get_last_token().atr(), 0,0, [], []) # esta mal, hay que calcular lo de parametros y desplazamiento
                        #         self.totalNumTablas += 1
                        #         self.tablaActual = self.totalNumTablas
                        #         tabla = tabladesimbolos.tabla_de_simbolos()
                        #         self.tables.append(tabla)
                        #         self.nombreUltFuncion = value
                        #         self.desplazamiento = -1

                        #     elif (self.tablaActual != 0 and self.get_last_token().atr() != 'return'): # lo añades a la tabla de la funcion
                        #         self.entrada = self.symbol_table.getEntradasTS(self.nombreUltFuncion)
                        #         n = self.entrada.getNumero_parametros() + 1
                        #         self.entrada.setNumero_parametros(n)
                        #         parametros = self.entrada.getTipo_parametros()
                        #         parametros.append(self.get_last_token().atr())
                        #         self.entrada.setTipo_parametros(parametros)

                        #         if (self.get_last_token().atr() == 'cad'):
                        #             self.desplazamiento += len(value)
                        #         else:
                        #             self.desplazamiento += 1

                        #         self.tables[self.tablaActual - 1].addEntrada(value, self.get_last_token().atr(), self.desplazamiento, 0, [], [])
                                
                        #     elif (self.get_last_token().atr() != 'return'):
                        #         self.desplazamiento = self.symbol_table.getUltimoDesp()
                        #         if (self.get_last_token().atr() == 'cad'):
                                    
                                #     self.desplazamiento += len(value)
                                # else:
                                #     self.desplazamiento += 1
                                
                                # self.symbol_table.addEntrada(value)
                                # # self.symbol_table.addEntrada(value, self.get_last_token().atr(), self.desplazamiento, 0, [], [])
                                # self.symbol_table.setUltimoDesp(self.desplazamiento)

                        # else: # si no es funcion, lo añades a la tabla global
                        #     self.desplazamiento = self.symbol_table.getUltimoDesp()
                        #     if (self.get_last_token().atr() == 'cad'):
                        #         self.desplazamiento += len(value)
                        #     else:
                        #         self.desplazamiento += 1

                        #     self.symbol_table.addEntrada(value) 
                        #     # self.symbol_table.addEntrada(value, None, self.desplazamiento, 0, [], [])
                        #     # self.symbol_table.addEntrada(value, self.get_last_token().atr(), self.desplazamiento, 0, [], [])
                        #     self.symbol_table.setUltimoDesp(self.desplazamiento)
