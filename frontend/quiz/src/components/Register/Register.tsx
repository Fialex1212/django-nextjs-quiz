import React from "react";
import cn from "classnames";
import Link from "next/link";
import Image from "next/image";
import css from "./styles.module.css";

import google from "@/app/static/icons/login/google-icon.svg";
import twitter from "@/app/static/icons/login/twitter-icon.svg";
import apple from "@/app/static/icons/login/apple-icon.svg";
import profile from "@/app/static/icons/login/profile.png";

const Register = () => {
  return (
    <section className={css.login}>
      <div className="container">
        <div className={css.login__wrapper}>
          <form className={css.form}>
            <div className={css.form__header}>
              <div className={css.profile__wrapper}>
                <Image
                  className={css.login__profile}
                  src={profile}
                  alt="profile"
                  width={50}
                  height={50}
                />
              </div>
              <h3 className={css.login__title}>Wellcome</h3>
              <p className={css.login__subtitle}>
                Please enter your information to register
              </p>
            </div>
            <ul className={css.social__list}>
              <li className={css.social__item}>
                <Image
                  className={css.image}
                  src={apple}
                  alt="apple"
                  width={30}
                  height={30}
                />
              </li>
              <li className={css.social__item}>
                <Image src={google} alt="google" width={30} height={30} />
              </li>
              <li className={css.social__item}>
                <Image src={twitter} alt="twitter" width={30} height={30} />
              </li>
            </ul>
            <div className={css.or}>OR</div>
            <label
              className={cn(css.input__wrapper, css.input__wrapper__first)}
            >
              <label className={css.input__title}>Email Address</label>
              <input
                className={css.form__input}
                type="email"
                placeholder="Enter your email..."
              />
            </label>
            <label
              className={cn(css.input__wrapper, css.input__wrapper__second)}
            >
              <label className={css.input__title}>Password</label>
              <input
                className={css.form__input}
                type="password"
                placeholder="Enter your password..."
              />
            </label>
            <label
              className={cn(css.input__wrapper, css.input__wrapper__third)}
            >
              <label className={css.input__title}>Repeate Password</label>
              <input
                className={css.form__input}
                type="password"
                placeholder="Repeate your password..."
              />
            </label>
            <button className={css.form__button} type="submit">
              Login
            </button>
            <p className={css.form__redirect}>
              Already have an account?{" "}
              <Link className={css.register__link} href="/login">
                Login
              </Link>
            </p>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Register;
