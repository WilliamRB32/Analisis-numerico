library(readxl)
library(dplyr)
library(Matrix)
library(PolynomF)
library(pracma)
library(splines)

#datos
#random
aleatorios<-c(sample(1:586,469,replace = F))
aleatorios<-sort(aleatorios, decreasing = FALSE)
#tabla inicial temperatura 
Crato_fullTemp<- read_excel("semestre/Analisis/Reto 2/Informacion.xlsx",
                            sheet = "Crato", range = "d1:d586")
#tabla con ID
Crato_fullTemp<-data.frame(ID=1:nrow(Crato_fullTemp),temperatura=Crato_fullTemp$`Temp. Interna (ºC)`)
#tabla limitada con el 80% de manera random
Crato_modeloTemp<-Crato_fullTemp[aleatorios, ]
#Tabla inicial hora
Crato_fullHora<- read_excel("semestre/Analisis/Reto 2/Informacion.xlsx",
                            sheet = "Crato", range = "c1:c586")
#tabla con ID
Crato_fullHora<-data.frame(ID=1:nrow(Crato_fullHora),Hora=Crato_fullHora$`Hora`)
#tabla limitada con el 80%
Crato_modeloHora<-Crato_fullHora[aleatorios, ]

#tabla con las temperaturas restantes y horas restandes (20%)
Crato_TempEx<-Crato_fullTemp[-aleatorios, ]
Crato_HoraEx<-Crato_fullHora[-aleatorios, ]

#tablas del segundo punto 
Jati_modeloTemp <- read_excel("semestre/Analisis/Reto 2/Informacion.xlsx", 
                              sheet = "jati", range = "d1:d720")
Jati_modeloHora <- read_excel("semestre/Analisis/Reto 2/Informacion.xlsx", 
                              sheet = "jati", range = "c1:c720")



#=============================
#error punto a punto
ErrorPxP = function(h)
{
  cont = 1
  pos = 1
  errorP = vector("numeric", length(Crato_TempEx$temperatura))
  
  repeat
  {
    if((cont == Crato_HoraEx$Hora[pos]))
    {
      errorP[pos] = abs(h(cont) - Crato_TempEx$temperatura[pos])
      pos = pos + 1
    }
    if(cont == length(Crato_fullHora$Hora) || pos == length(Crato_TempEx$temperatura)) break
    cont = cont + 1
    
  }
  return (errorP)
}
#error cuadratico medio
ErrorCuadraticoM = function (h)
{
  cont = 1
  pos = 1
  valorT = 0
  repeat
  {
    if(cont == Crato_HoraEx$Hora[pos])
    {
      #Crato_TempEx es mi valor Observado y h es mi valor Estimado
      valorT = valorT + (Crato_TempEx$temperatura[pos] - h(cont))^2
      pos = pos + 1
    }
    if(cont == length(Crato_fullHora$Hora) || pos == length(Crato_TempEx$temperatura)) break
    cont = cont + 1
  }
  valorT = valorT / length(Crato_TempEx$temperatura)
  return (valorT)
}


ErrorProm = function(vectoRs)
{
  cont = 1
  Promedio = 0
  repeat
  {
    Promedio = vectoRs[cont] + Promedio
    if(cont == length(vectoRs)) break
    cont = cont + 1
  }
  Promedio = Promedio / length(vectoRs)
  return(Promedio)
}



plot(Crato_fullHora$Hora,Crato_fullTemp$temperatura,type = "l",ylab = "Temperatura Interna",xlab = "Horas",main = "Tempertura Interna en el tiempo (Crato)",ylim=c(-55,90),xlim=c(0,2400))
plot(Jati_modeloHora$Hora,Jati_modeloTemp$`Temp. Interna (ºC)`,type = "l",ylab = "Temperatura Interna",xlab = "Horas",main = "Tempertura Interna en el tiempo (Jati)",ylim=c(14,44),xlim=c(0,2400))


h <- splinefun(Crato_modeloHora$Hora,Crato_modeloTemp$temperatura, method = "fmm", ties = mean)
h(469)

par(new=TRUE)
plot(h,ylim=c(0,50),xlim=c(0,2400),col="green",ann=F)

#Grafica del spline
par(new=FALSE)
plot(h,ylim=c(0,50),xlim=c(0,2400),col="green",type = "l",ylab = "Temperatura Interna",xlab = "Horas",main = "Spliene - Tempertura Interna en el tiempo (Crato)")

# Calculo de errores

VectorErrores <- ErrorPxP (h)

#Promedio de Error.
NoPromedio <-ErrorProm(VectorErrores)
cat(NoPromedio)

#Vecino cercano
ErrorPxPVecino = function(h){
  cont = 1
  pos = 1
  errorP <- c()
  repeat
  {
    errorP <- c(errorP, abs(h(Jati_modeloHora$Hora[pos])-Jati_modeloTemp$`Temp. Interna (ºC)`[pos]))
    pos = pos + 1
    if(pos > length(Jati_modeloHora$Hora)){
      break
    }
  }
  return (errorP)
}

VectorErrores <- ErrorPxP (h)

#Promedio de Error.
NoPromedio <-ErrorProm(VectorErrores)

#Grafica de Errores Punto por Punto
plot(Crato_HoraEx$Hora,VectorErrores,ylab = "Error - Temperatura Interna", xlab = "Horas", main = "Error: Temperatura Interna vs Horas", ylim=c(0,4.5),xlim=c(0,730))
err <- splinefun(Crato_HoraEx$Hora,VectorErrores, method = "fmm", ties = mean)
plot(err ,ylab = "Temperatura Interna", xlab = "Horas", main ="Interpolación Error", ylim=c(0,5),xlim=c(0,585), col = "blue", ann = F)

#ErrorCuadradoMedio y ErrorAbsolutoMedio
cat("Se miden dos errores para analizar la estimación.\n")
cat("A continuación, tenemos el Error Cuadratico Medio: ")
MedioCuadrado = ErrorCuadraticoM(h)
cat(MedioCuadrado)
cat("\nError Absoluto Medio: ")
cat(NoPromedio)

errorPuntoVecino <- ErrorPxPVecino(h)
#Grafica error punto a punto vecino mas cercano
plot(Jati_modeloHora$Hora,errorPuntoVecino, pch = 1,col = "red")
#error promedio vecino mas cercano
errorPromVecino <- ErrorProm(errorPuntoVecino)
errorPromVecino
#error maximo 
max(errorPuntoVecino)
#error minimo
min(errorPuntoVecino)

