CREATE TABLE rooms (
  room_number NUMBER PRIMARY KEY, 
  room_view TEXT NOT NULL,
  price REAL NOT NULL,
  availability BOOLEAN DEFAULT 1
);

CREATE TABLE guests (
  passport INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT NOT NULL,
  phone_number INTEGER
);

CREATE TABLE bookings (
  booking_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  guest_passport INTEGER NOT NULL,
  room_number NUMBER NOT NULL,
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  total_amount REAL NOT NULL,
  FOREIGN KEY (guest_passport) REFERENCES guests (passport),
  FOREIGN KEY (room_number) REFERENCES rooms (room_number)
);

CREATE TABLE services (
  service_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  service_name TEXT NOT NULL,
  price REAL NOT NULL
);

CREATE TABLE billing (
  billing_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  booking_id INTEGER NOT NULL, 
  service_id INTEGER NOT NULL, 
  amount REAL NOT NULL,
  FOREIGN KEY (booking_id) REFERENCES bookings (booking_id),
  FOREIGN KEY (service_id) REFERENCES services (service_id)
);
