from sqlalchemy import text
from data.database import engine


def trigger_exists(conn, trigger_name):
    result = conn.execute(text("""
        SELECT TRIGGER_NAME
        FROM information_schema.TRIGGERS
        WHERE TRIGGER_SCHEMA = DATABASE()
        AND TRIGGER_NAME = :name
    """), {"name": trigger_name})

    return result.fetchone() is not None


def create_movie_triggers():

    triggers = {
        "movie_check_date": """
        -- Kiểm tra ngày khi INSERT
        CREATE TRIGGER movie_check_date
        BEFORE INSERT ON movies
        FOR EACH ROW
        BEGIN
            IF NEW.release_date >= NEW.end_date THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'release_date phải nhỏ hơn end_date';
            END IF;
        END
        """,

        "movie_check_date_update": """
        -- Kiểm tra ngày khi UPDATE
        CREATE TRIGGER movie_check_date_update
        BEFORE UPDATE ON movies
        FOR EACH ROW
        BEGIN
            IF NEW.release_date >= NEW.end_date THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'release_date phải nhỏ hơn end_date';
            END IF;
        END
        """,
        
        "showtime_check_dayshow_insert": """
        -- Kiểm tra dayshow khi INSERT showtime
        CREATE TRIGGER showtime_check_dayshow_insert
        BEFORE INSERT ON showtimes
        FOR EACH ROW
        BEGIN
            DECLARE v_release_date DATE;
            DECLARE v_end_date DATE;

            -- Lấy ngày chiếu và ngày kết thúc của bộ phim tương ứng
            SELECT release_date, end_date INTO v_release_date, v_end_date
            FROM movies
            WHERE id = NEW.movie_id;

            -- So sánh dayshow với khoảng thời gian chiếu
            IF NEW.dayshow < v_release_date OR NEW.dayshow > v_end_date THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Lỗi: dayshow phải nằm trong khoảng từ release_date đến end_date của phim';
            END IF;
        END
        """,

        "showtime_check_dayshow_update": """
        -- Kiểm tra dayshow khi UPDATE showtime
        CREATE TRIGGER showtime_check_dayshow_update
        BEFORE UPDATE ON showtimes
        FOR EACH ROW
        BEGIN
            DECLARE v_release_date DATE;
            DECLARE v_end_date DATE;

            SELECT release_date, end_date INTO v_release_date, v_end_date
            FROM movies
            WHERE id = NEW.movie_id;

            IF NEW.dayshow < v_release_date OR NEW.dayshow > v_end_date THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Lỗi: dayshow phải nằm trong khoảng từ release_date đến end_date của phim';
            END IF;
        END
        """
    }

    with engine.connect() as conn:

        for name, sql in triggers.items():

            if not trigger_exists(conn, name):
                conn.execute(text(sql))
                print(f"Trigger {name} created")
            else:
                print(f"Trigger {name} already exists")

        conn.commit()

    print("Trigger check completed")