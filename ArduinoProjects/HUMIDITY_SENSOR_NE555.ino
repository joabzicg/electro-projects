// Arduino Frequency to Voltage converter without the aid of ICs - 2012 \\ adaptado para sensor de umidade ><><><><><> By Joab

int DigitalIn13 = 13; //Input of pulses
int DigitalIn12 = 12; //Input of pulses
int DigitalIn11 = 11; //Input of pulses
int C = 2; // SAÍDA C
int B = 3; // SAÍDA B
int A = 4; // SAÍDA A
float Frequency = 0; //Frequency of the pulses
float Frequency2 = 1; //Frequency of the pulses
float Frequency3 = 50; //Frequency of the pulses
unsigned long HighTime; //the HIGH time of pulses
unsigned long HighTime2; //the HIGH time of pulses
unsigned long HighTime3; //the HIGH time of pulses
unsigned long LowTime; //the LOW time of pulses
unsigned long LowTime2; //the LOW time of pulses
unsigned long LowTime3; //the LOW time of pulses
unsigned long Period; //period = HighTime + LowTime
unsigned long Period2; //period = HighTime + LowTime
unsigned long Period3; //period = HighTime + LowTime
unsigned int volt = 0; // Variable to hold the voltage read
unsigned int volt2 = 0; // Variable to hold the voltage read
unsigned int volt3 = 0; // Variable to hold the voltage read


void setup() {
   Serial.begin(9600);
   pinMode(DigitalIn13, INPUT); //sets pulses pin as input
   pinMode(DigitalIn12, INPUT); // LED definido como saída
   pinMode(DigitalIn11, INPUT); // LED definido como saída
   pinMode(A, OUTPUT); // LED definido como saída
   pinMode(B, OUTPUT); // LED definido como saída
   pinMode(C, OUTPUT); // LED definido como saída
   
}

void loop() {
 // PARTE CONVERSÃO FREQUÊNCIA - VOLTS   #SENSOR 1# 
 HighTime = pulseIn(DigitalIn13, HIGH); //the HIGH time of pulses in ms
 LowTime = pulseIn(DigitalIn13, LOW); //the LOW time of pulses
 Period = HighTime + LowTime; //period
 Frequency = 1/(Period * 0.000001); //Frequency
 volt = map(Frequency, 0, 242, 0, 255); //maps the frequency into voltage
 Serial.println(volt); // Mostrando valores no serial para voltagem (altere para volt2 ou volt3 para ver os outros sensores)
 // NÍVEL BAIXO
 if (volt < 27) {
  digitalWrite(A, LOW); // Colocando a saída A como 0 ( NIVEL BAIXO)
  digitalWrite(B, LOW); // Colocando a saída B como 0 ( NIVEL BAIXO)
  digitalWrite(C, HIGH); // Colocando a saída C como 1 ( NIVEL BAIXO)
 }
 else {
  digitalWrite(A, LOW); // Colocando a saída A como 0 ( SECO)
  digitalWrite(B, LOW); // Colocando a saída B como 0 ( SECO)
  digitalWrite(C, LOW); // Colocando a saída C como 0 ( SECO)
 }
  // PARTE CONVERSÃO FREQUÊNCIA - VOLTS   #SENSOR 2# 
 HighTime2 = pulseIn(DigitalIn12, HIGH); //the HIGH time of pulses in ms
 LowTime2 = pulseIn(DigitalIn12, LOW); //the LOW time of pulses
 Period2 = HighTime2 + LowTime2; //period
 Frequency2 = 1/(Period2 * 0.000001); //Frequency
 volt2 = map(Frequency2, 0, 242, 0, 255); //maps the frequency into voltage
 // NÍVEL MÉDIO
 if (volt2 < 27) {
  digitalWrite(A, LOW); // Colocando a saída A como 0 ( NIVEL MÉDIO)
  digitalWrite(B, HIGH); // Colocando a saída B como 1 ( NIVEL MÉDIO)
  digitalWrite(C, LOW); // Colocando a saída C como 0 ( NIVEL MÉDIO)
 }
 else {
  digitalWrite(A, LOW); // Colocando a saída A como 0 ( NIVEL BAIXO)
  digitalWrite(B, LOW); // Colocando a saída B como 0 ( NIVEL BAIXO)
  digitalWrite(C, HIGH); // Colocando a saída C como 1 ( NIVEL BAIXO)
 }
 // PARTE CONVERSÃO FREQUÊNCIA - VOLTS   #SENSOR 3# 
 HighTime3 = pulseIn(DigitalIn11, HIGH); //the HIGH time of pulses in ms
 LowTime3 = pulseIn(DigitalIn11, LOW); //the LOW time of pulses
 Period3 = HighTime3 + LowTime3; //period
 Frequency3 = 1/(Period3 * 0.000001); //Frequency
 volt3 = map(Frequency3, 0, 242, 0, 255); //maps the frequency into voltage
 // NÍVEL ALTO
 if (volt3 < 27) {
  digitalWrite(A, HIGH); // Colocando a saída A como 1 ( NIVEL ALTO)
  digitalWrite(B, LOW); // Colocando a saída B como 0 ( NIVEL ALTO)
  digitalWrite(C, LOW); // Colocando a saída C como 0 ( NIVEL ALTO)
 }
 else {
  digitalWrite(A, LOW); // COLOCANDO A SAÍDA A COMO 0 (NÍVEL MEDIO)
  digitalWrite(B, HIGH); // Colocando a saída B como 1 ( NIVEL MEDIO)
  digitalWrite(C, LOW); // Colocando a saída C como 0 ( NIVEL MEDIO)
 }
 
}
