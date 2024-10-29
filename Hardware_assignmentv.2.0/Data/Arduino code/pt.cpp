const int analogPin = A0;  // Pin to read voltage across PT-100
const float vRef = 5.0;    // Reference voltage (5V from Arduino)

void setup() {
  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  // Read the analog value (0-1023)
  int sensorValue = analogRead(analogPin);

  // Convert the analog reading to voltage
  float voltageAcrossPT100 = (vRef * sensorValue) / 1023.0;

  // Print the measured voltage
  Serial.print("Voltage across PT-100: ");
  Serial.print(voltageAcrossPT100);
  Serial.println(" V");

  delay(1000);  // Delay for 1 second before taking another reading
}
